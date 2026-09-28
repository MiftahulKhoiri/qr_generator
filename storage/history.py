"""Riwayat QR Code yang pernah dibuat (disimpan sebagai JSON)."""

import json
from datetime import datetime
from pathlib import Path

HISTORY_FILE = Path(__file__).resolve().parent / "history.json"
MAX_ENTRIES = 200


def load_history(history_file=HISTORY_FILE):
    path = Path(history_file)
    if not path.exists():
        return []
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return []
    return data if isinstance(data, list) else []


def _save(entries, history_file):
    path = Path(history_file)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)


def add_entry(data, image_path, history_file=HISTORY_FILE):
    entries = load_history(history_file)
    entry = {
        "waktu": datetime.now().isoformat(timespec="seconds"),
        "data": data,
        "file": str(image_path),
    }
    entries.append(entry)
    _save(entries[-MAX_ENTRIES:], history_file)
    return entry


def clear_history(history_file=HISTORY_FILE):
    _save([], history_file)
