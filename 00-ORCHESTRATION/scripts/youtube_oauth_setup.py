#!/usr/bin/env python3
"""
YouTube OAuth2 Setup Script for Syncrescendence Source Ingest Pipeline.

Authenticates with Google OAuth2 for installed (desktop) applications.
Saves token to ~/.syncrescendence/youtube_token.json.

Prerequisites:
  1. Create OAuth2 Desktop credentials at console.cloud.google.com
  2. Download client_secret.json to ~/.syncrescendence/client_secret.json
  3. pip install google-auth-oauthlib google-api-python-client

Usage:
  python youtube_oauth_setup.py
  python youtube_oauth_setup.py --client-secret /path/to/client_secret.json
"""

import argparse
import json
import os
import sys
from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

SYNCRESCENDENCE_DIR = Path(os.environ.get(
    "SYNCRESCENDENCE_CONFIG_DIR",
    Path.home() / ".syncrescendence"
))

DEFAULT_CLIENT_SECRET = SYNCRESCENDENCE_DIR / "client_secret.json"
DEFAULT_TOKEN_PATH = SYNCRESCENDENCE_DIR / "youtube_token.json"

SCOPES = [
    "https://www.googleapis.com/auth/youtube.readonly",
    "https://www.googleapis.com/auth/youtube",
]


def setup_oauth(client_secret_path: Path, token_path: Path) -> Credentials:
    """Run OAuth2 consent flow and save token."""

    if not client_secret_path.exists():
        print(f"ERROR: client_secret.json not found at {client_secret_path}")
        print()
        print("To create it:")
        print("  1. Go to https://console.cloud.google.com/apis/credentials")
        print("  2. Create Credentials -> OAuth client ID -> Desktop app")
        print("  3. Download the JSON and save it to:")
        print(f"     {client_secret_path}")
        sys.exit(1)

    # Check for existing valid token
    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
        if creds and creds.valid:
            print(f"Existing valid token found at {token_path}")
            print("Re-run with --force to re-authenticate.")
            return creds
        if creds and creds.expired and creds.refresh_token:
            print("Token expired, refreshing...")
            creds.refresh(Request())
            _save_token(creds, token_path)
            print(f"Token refreshed and saved to {token_path}")
            return creds

    # Run full OAuth flow
    print("Starting OAuth2 consent flow...")
    print("A browser window will open. Approve access to your YouTube account.")
    print()

    flow = InstalledAppFlow.from_client_secrets_file(
        str(client_secret_path), SCOPES
    )
    creds = flow.run_local_server(port=0)

    _save_token(creds, token_path)
    print()
    print(f"Token saved to {token_path}")
    print("YouTube OAuth2 setup complete.")
    return creds


def _save_token(creds: Credentials, token_path: Path):
    """Save credentials to JSON file with restricted permissions."""
    token_path.parent.mkdir(parents=True, exist_ok=True)
    token_data = {
        "token": creds.token,
        "refresh_token": creds.refresh_token,
        "token_uri": creds.token_uri,
        "client_id": creds.client_id,
        "client_secret": creds.client_secret,
        "scopes": creds.scopes and list(creds.scopes),
    }
    token_path.write_text(json.dumps(token_data, indent=2))
    os.chmod(token_path, 0o600)


def main():
    parser = argparse.ArgumentParser(
        description="Set up YouTube OAuth2 for Syncrescendence ingest pipeline"
    )
    parser.add_argument(
        "--client-secret",
        type=Path,
        default=DEFAULT_CLIENT_SECRET,
        help=f"Path to client_secret.json (default: {DEFAULT_CLIENT_SECRET})",
    )
    parser.add_argument(
        "--token-path",
        type=Path,
        default=DEFAULT_TOKEN_PATH,
        help=f"Path to save token (default: {DEFAULT_TOKEN_PATH})",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force re-authentication even if valid token exists",
    )
    args = parser.parse_args()

    if args.force and args.token_path.exists():
        args.token_path.unlink()

    setup_oauth(args.client_secret, args.token_path)


if __name__ == "__main__":
    main()
