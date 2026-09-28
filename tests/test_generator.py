import pytest

from qr.generator import generate_qr
from qr.validator import ValidationError


def test_generate_png(tmp_path):
    path = generate_qr("https://example.com", filename="tes", output_dir=tmp_path)
    assert path == tmp_path / "tes.png"
    assert path.read_bytes().startswith(b"\x89PNG")


def test_generate_svg(tmp_path):
    path = generate_qr("halo", filename="tes", fmt="svg", output_dir=tmp_path)
    assert path.suffix == ".svg"
    assert b"<svg" in path.read_bytes()


def test_ekstensi_di_nama_file_tidak_dobel(tmp_path):
    path = generate_qr("halo", filename="tes.png", output_dir=tmp_path)
    assert path.name == "tes.png"


def test_nama_otomatis(tmp_path):
    path = generate_qr("halo", output_dir=tmp_path)
    assert path.name.startswith("qr_")
    assert path.exists()


def test_input_tidak_valid(tmp_path):
    with pytest.raises(ValidationError):
        generate_qr("", output_dir=tmp_path)
    with pytest.raises(ValidationError):
        generate_qr("halo", filename="../hack", output_dir=tmp_path)
