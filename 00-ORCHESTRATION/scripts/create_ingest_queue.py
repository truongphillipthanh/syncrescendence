#!/usr/bin/env python3
"""
Create the "Ingest Queue" private playlist on YouTube.

Uses the same OAuth2 token as youtube_ingest.py.
Saves the playlist ID to ~/.syncrescendence/ingest_queue_playlist_id.txt.

Usage:
  python create_ingest_queue.py
"""

import json
import os
import sys
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build as build_youtube

SYNCRESCENDENCE_DIR = Path(os.environ.get(
    "SYNCRESCENDENCE_CONFIG_DIR",
    Path.home() / ".syncrescendence"
))

TOKEN_PATH = SYNCRESCENDENCE_DIR / "youtube_token.json"
PLAYLIST_ID_PATH = SYNCRESCENDENCE_DIR / "ingest_queue_playlist_id.txt"

SCOPES = [
    "https://www.googleapis.com/auth/youtube.readonly",
    "https://www.googleapis.com/auth/youtube",
]


def get_authenticated_service():
    if not TOKEN_PATH.exists():
        print(f"ERROR: Token not found at {TOKEN_PATH}. Run youtube_oauth_setup.py first.")
        sys.exit(1)

    creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)

    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        token_data = {
            "token": creds.token,
            "refresh_token": creds.refresh_token,
            "token_uri": creds.token_uri,
            "client_id": creds.client_id,
            "client_secret": creds.client_secret,
            "scopes": list(creds.scopes) if creds.scopes else None,
        }
        TOKEN_PATH.write_text(json.dumps(token_data, indent=2))
        os.chmod(TOKEN_PATH, 0o600)

    if not creds.valid:
        print("ERROR: Token invalid. Re-run youtube_oauth_setup.py.")
        sys.exit(1)

    return build_youtube("youtube", "v3", credentials=creds)


def main():
    # Check if already created
    if PLAYLIST_ID_PATH.exists():
        existing_id = PLAYLIST_ID_PATH.read_text().strip()
        if existing_id:
            print(f"Ingest Queue playlist already exists: {existing_id}")
            print(f"Stored at: {PLAYLIST_ID_PATH}")
            print("Delete that file to create a new one.")
            return

    youtube = get_authenticated_service()

    response = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": "Ingest Queue",
                "description": "Stateless inbox-zero ingest queue for Syncrescendence. "
                               "Videos added here are automatically processed and removed.",
            },
            "status": {
                "privacyStatus": "private",
            },
        },
    ).execute()

    playlist_id = response["id"]

    PLAYLIST_ID_PATH.write_text(playlist_id + "\n")

    print(f"Created playlist: Ingest Queue")
    print(f"Playlist ID: {playlist_id}")
    print(f"URL: https://www.youtube.com/playlist?list={playlist_id}")
    print(f"Saved to: {PLAYLIST_ID_PATH}")


if __name__ == "__main__":
    main()
