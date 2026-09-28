"""Validasi input untuk pembuatan QR Code."""

import re

MAX_LENGTH = 1000
MAX_FILENAME = 100
VALID_ERROR_LEVELS = ("L", "M", "Q", "H")
VALID_FORMATS = ("png", "svg")
_FILENAME_RE = re.compile(r"^[A-Za-z0-9._-]+$")


class ValidationError(ValueError):
    """Dilempar ketika input tidak valid."""


def validate_text(text):
    if text is None or not str(text).strip():
        raise ValidationError("Teks tidak boleh kosong.")
    text = str(text).strip()
    if len(text) > MAX_LENGTH:
        raise ValidationError(f"Teks terlalu panjang (maks {MAX_LENGTH} karakter).")
    return text


def validate_filename(name):
    name = str(name).strip()
    if not name:
        raise ValidationError("Nama file tidak boleh kosong.")
    if len(name) > MAX_FILENAME:
        raise ValidationError(f"Nama file terlalu panjang (maks {MAX_FILENAME} karakter).")
    if name.startswith(".") or not _FILENAME_RE.match(name):
        raise ValidationError(
            "Nama file hanya boleh huruf, angka, titik, strip, dan underscore "
            "(tidak boleh diawali titik)."
        )
    return name


def validate_error_level(level):
    level = str(level).strip().upper()
    if level not in VALID_ERROR_LEVELS:
        raise ValidationError("Level koreksi error harus salah satu dari: L, M, Q, H.")
    return level


def validate_format(fmt):
    fmt = str(fmt).strip().lower()
    if fmt not in VALID_FORMATS:
        raise ValidationError("Format harus 'png' atau 'svg'.")
    return fmt


def validate_scale(scale):
    try:
        scale = int(scale)
    except (TypeError, ValueError):
        raise ValidationError("Skala harus berupa angka bulat.")
    if not 1 <= scale <= 50:
        raise ValidationError("Skala harus antara 1 dan 50.")
    return scale
