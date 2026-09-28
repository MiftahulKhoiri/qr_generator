"""Logika membuat QR Code."""

from datetime import datetime
from pathlib import Path

import segno

from qr.validator import (
    VALID_FORMATS,
    ValidationError,
    validate_error_level,
    validate_filename,
    validate_format,
    validate_scale,
    validate_text,
)

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"


def _default_filename():
    return datetime.now().strftime("qr_%Y%m%d_%H%M%S")


def _strip_extension(name):
    lower = name.lower()
    for ext in VALID_FORMATS:
        if lower.endswith(f".{ext}"):
            return name[: -(len(ext) + 1)]
    return name


def _make(data, error):
    try:
        return segno.make(data, error=error, micro=False)
    except segno.DataOverflowError:
        raise ValidationError("Data terlalu besar untuk dijadikan QR Code.")


def generate_qr(data, filename=None, output_dir=OUTPUT_DIR,
                fmt="png", error="M", scale=10, border=4):
    """Buat QR Code lalu simpan ke file. Mengembalikan Path file hasil."""
    data = validate_text(data)
    fmt = validate_format(fmt)
    error = validate_error_level(error)
    scale = validate_scale(scale)

    if filename:
        filename = _strip_extension(validate_filename(filename))
    else:
        filename = _default_filename()

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"{filename}.{fmt}"

    qr = _make(data, error)
    qr.save(str(path), scale=scale, border=border)
    return path


def preview_terminal(data, error="M"):
    """Tampilkan QR Code langsung di terminal."""
    data = validate_text(data)
    error = validate_error_level(error)
    _make(data, error).terminal(compact=True)
