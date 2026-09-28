"""Tampilan aplikasi (menu terminal)."""

from qr.generator import generate_qr, preview_terminal
from qr.validator import ValidationError
from storage.history import add_entry, clear_history, load_history

MENU = """
=== QR Code Generator ===
1. Buat QR Code
2. Lihat riwayat
3. Hapus riwayat
0. Keluar
"""


def _ask(prompt, default=None):
    suffix = f" [{default}]" if default else ""
    value = input(f"{prompt}{suffix}: ").strip()
    return value or default


def create_qr():
    text = input("Teks / URL: ").strip()
    filename = _ask("Nama file (kosongkan = otomatis)")
    fmt = _ask("Format (png/svg)", "png")
    error = _ask("Level koreksi error (L/M/Q/H)", "M")

    try:
        path = generate_qr(text, filename=filename, fmt=fmt, error=error)
    except ValidationError as e:
        print(f"Gagal: {e}")
        return

    add_entry(text, path)
    print(f"QR Code tersimpan: {path}")

    if _ask("Tampilkan di terminal? (y/n)", "n").lower() == "y":
        preview_terminal(text, error=error)


def show_history():
    entries = load_history()
    if not entries:
        print("Riwayat masih kosong.")
        return
    for i, e in enumerate(entries, 1):
        data = e.get("data", "")
        if len(data) > 40:
            data = data[:37] + "..."
        print(f"{i:>3}. [{e.get('waktu', '-')}] {data} -> {e.get('file', '-')}")


def clear():
    if _ask("Yakin hapus semua riwayat? (y/n)", "n").lower() == "y":
        clear_history()
        print("Riwayat dihapus.")
    else:
        print("Dibatalkan.")


def run():
    actions = {"1": create_qr, "2": show_history, "3": clear}
    while True:
        print(MENU)
        try:
            choice = input("Pilih menu: ").strip()
            if choice == "0":
                print("Sampai jumpa!")
                break
            action = actions.get(choice)
            if action:
                action()
            else:
                print("Pilihan tidak valid.")
        except (KeyboardInterrupt, EOFError):
            print("\nSampai jumpa!")
            break
