import pytest

from qr.validator import (
    MAX_LENGTH,
    ValidationError,
    validate_error_level,
    validate_filename,
    validate_format,
    validate_scale,
    validate_text,
)


def test_text_valid_dan_di_strip():
    assert validate_text("  halo  ") == "halo"


@pytest.mark.parametrize("bad", ["", "   ", None])
def test_text_kosong(bad):
    with pytest.raises(ValidationError):
        validate_text(bad)


def test_text_terlalu_panjang():
    with pytest.raises(ValidationError):
        validate_text("a" * (MAX_LENGTH + 1))


def test_filename_valid():
    assert validate_filename("qr_saya-1.v2") == "qr_saya-1.v2"


@pytest.mark.parametrize("bad", ["", "../hack", "a/b", "..", ".rahasia", "nama file"])
def test_filename_tidak_valid(bad):
    with pytest.raises(ValidationError):
        validate_filename(bad)


def test_error_level():
    assert validate_error_level("h") == "H"
    with pytest.raises(ValidationError):
        validate_error_level("X")


def test_format():
    assert validate_format("PNG") == "png"
    with pytest.raises(ValidationError):
        validate_format("jpg")


def test_scale():
    assert validate_scale("10") == 10
    with pytest.raises(ValidationError):
        validate_scale(0)
    with pytest.raises(ValidationError):
        validate_scale("abc")
