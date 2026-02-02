#!/usr/bin/env python3
"""
sync_ledgers.py
Atomic ledger synchronization with validation.

Usage:
    python sync_ledgers.py --ledger tasks --action add --data '{"id":"TASK-XXX",...}'
    python sync_ledgers.py --ledger tasks --action update --id TASK-001 --field status --value done
    python sync_ledgers.py --validate
"""

import argparse
import csv
import json
import os
import shutil
from datetime import datetime
from pathlib import Path

# Ledger paths (relative to repo root)
LEDGERS = {
    'tasks': Path('00-ORCHESTRATION/state/DYN-TASKS.csv'),
    'projects': Path('00-ORCHESTRATION/state/DYN-PROJECTS.csv'),
    'sources': Path('04-SOURCES/DYN-SOURCES.csv'),
}

# Required columns per ledger
REQUIRED_COLUMNS = {
    'tasks': ['id', 'project_id', 'name', 'type', 'status', 'priority', 'owner'],
    'projects': ['id', 'name', 'type', 'status', 'priority', 'owner'],
    'sources': ['id', 'filename', 'status'],
}


def get_repo_root() -> Path:
    """Find repository root by looking for .git directory."""
    current = Path.cwd()
    while current != current.parent:
        if (current / '.git').exists():
            return current
        current = current.parent
    return Path.cwd()


def backup_ledger(ledger_path: Path) -> Path:
    """Create timestamped backup."""
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    backup_path = ledger_path.with_suffix(f'.csv.bak.{timestamp}')
    shutil.copy(ledger_path, backup_path)
    return backup_path


def validate_ledger(ledger_name: str) -> tuple[bool, str]:
    """Validate ledger structure and content."""
    repo_root = get_repo_root()
    path = repo_root / LEDGERS.get(ledger_name)

    if not path or not path.exists():
        return False, f"Ledger not found: {ledger_name}"

    required = REQUIRED_COLUMNS.get(ledger_name, [])

    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []

        # Check required columns
        missing = [col for col in required if col not in headers]
        if missing:
            return False, f"Missing columns: {missing}"

        # Check for malformed rows
        row_count = 0
        for row in reader:
            row_count += 1
            if len(row) != len(headers):
                return False, f"Malformed row {row_count}: column count mismatch"

    return True, f"Valid: {row_count} rows"


def atomic_write(ledger_path: Path, rows: list, fieldnames: list) -> bool:
    """Write ledger atomically via temp file."""
    temp_path = ledger_path.with_suffix('.csv.tmp')

    try:
        with open(temp_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        # Validate temp file
        with open(temp_path, 'r') as f:
            reader = csv.DictReader(f)
            temp_rows = list(reader)
            if len(temp_rows) != len(rows):
                raise ValueError("Row count mismatch after write")

        # Atomic rename
        os.replace(temp_path, ledger_path)
        return True

    except Exception as e:
        if temp_path.exists():
            temp_path.unlink()
        raise e


def add_row(ledger_name: str, data: dict) -> str:
    """Add row to ledger."""
    repo_root = get_repo_root()
    path = repo_root / LEDGERS[ledger_name]
    backup = backup_ledger(path)

    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    rows.append(data)
    atomic_write(path, rows, fieldnames)

    return f"Added row to {ledger_name}. Backup: {backup.name}"


def update_row(ledger_name: str, row_id: str, field: str, value: str) -> str:
    """Update specific field in row."""
    repo_root = get_repo_root()
    path = repo_root / LEDGERS[ledger_name]
    backup = backup_ledger(path)

    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    updated = False
    for row in rows:
        if row.get('id') == row_id:
            row[field] = value
            if 'updated' in fieldnames:
                row['updated'] = datetime.now().strftime('%Y-%m-%d')
            updated = True
            break

    if not updated:
        return f"Row not found: {row_id}"

    atomic_write(path, rows, fieldnames)
    return f"Updated {row_id}.{field} = {value}. Backup: {backup.name}"


def validate_all() -> None:
    """Validate all ledgers."""
    print("=== Ledger Validation ===\n")
    repo_root = get_repo_root()

    for name in LEDGERS:
        path = repo_root / LEDGERS[name]
        if path.exists():
            valid, message = validate_ledger(name)
            status = "+" if valid else "x"
            print(f"{status} {name}: {message}")
        else:
            print(f"- {name}: Not found at {path}")


def show_status() -> None:
    """Show summary of all ledgers."""
    print("=== Ledger Status ===\n")
    repo_root = get_repo_root()

    for name, rel_path in LEDGERS.items():
        path = repo_root / rel_path
        if path.exists():
            with open(path, 'r') as f:
                reader = csv.DictReader(f)
                rows = list(reader)

            # Count by status if status column exists
            if rows and 'status' in rows[0]:
                status_counts = {}
                for row in rows:
                    status = row.get('status', 'unknown')
                    status_counts[status] = status_counts.get(status, 0) + 1
                status_str = ', '.join(f"{k}:{v}" for k, v in sorted(status_counts.items()))
                print(f"{name}: {len(rows)} rows ({status_str})")
            else:
                print(f"{name}: {len(rows)} rows")
        else:
            print(f"{name}: Not found")


def main():
    parser = argparse.ArgumentParser(description='Ledger synchronization')
    parser.add_argument('--ledger', choices=list(LEDGERS.keys()))
    parser.add_argument('--action', choices=['add', 'update', 'validate'])
    parser.add_argument('--data', help='JSON data for add action')
    parser.add_argument('--id', help='Row ID for update action')
    parser.add_argument('--field', help='Field name for update action')
    parser.add_argument('--value', help='New value for update action')
    parser.add_argument('--validate', action='store_true', help='Validate all ledgers')
    parser.add_argument('--status', action='store_true', help='Show ledger status')

    args = parser.parse_args()

    if args.validate:
        validate_all()
        return

    if args.status:
        show_status()
        return

    if args.action == 'add':
        if not args.ledger or not args.data:
            print("Error: --ledger and --data required for add action")
            return
        data = json.loads(args.data)
        result = add_row(args.ledger, data)
        print(result)

    elif args.action == 'update':
        if not all([args.ledger, args.id, args.field, args.value]):
            print("Error: --ledger, --id, --field, and --value required for update action")
            return
        result = update_row(args.ledger, args.id, args.field, args.value)
        print(result)

    elif args.action == 'validate':
        if args.ledger:
            valid, message = validate_ledger(args.ledger)
            print(f"{'Valid' if valid else 'Invalid'}: {message}")
        else:
            validate_all()


if __name__ == '__main__':
    main()
