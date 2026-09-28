# QR Code Generator

Aplikasi terminal untuk membuat QR Code (PNG/SVG) dari teks atau URL,
lengkap dengan validasi input dan riwayat pembuatan.

## Struktur

- `main.py` : titik masuk aplikasi
- `qr/generator.py` : logika membuat QR Code
- `qr/validator.py` : validasi input
- `ui/app.py` : tampilan menu terminal
- `storage/history.py` : riwayat QR (disimpan di `storage/history.json`)
- `output/` : tempat gambar QR disimpan
- `tests/` : unit test

## Instalasi

    pip install -r requirements.txt

## Menjalankan

    python main.py

## Tes

    python -m pytest

## Catatan

- Level koreksi error: L (7%), M (15%), Q (25%), H (30%).
- Teks maksimal 1000 karakter.
- Pilih "Tampilkan di terminal" untuk melihat QR langsung tanpa membuka gambar.
