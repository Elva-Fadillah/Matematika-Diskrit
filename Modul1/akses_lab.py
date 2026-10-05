def cek_akses_laboratorium(mahasiswa_terdaftar, kartu_aktif, laboratorium_buka):
    if mahasiswa_terdaftar and kartu_aktif and laboratorium_buka:
        return "Akses Diterima: Selamat datang di laboratoriium"
    else:
        return "Akses Ditolak: Syarat askses tidak terpenuhi"

print("=== SIMULASI AKSES LABORATORIUM ===")

print("case 1: Semua syarat terpenuhi")
print("mahasiswa terdaftar: True")
print("kartu aktif: True")
print("laboratorium buka: True")
print( cek_akses_laboratorium(True, True, True))
print("-"* 50)

print("case 2: Laboratorium tutup")
print("mahasiswa terdaftar: True")
print("kartu aktif: True")
print("laboratorium buka: False")
print(cek_akses_laboratorium(True, True, False))
print("-"* 50)

print("case 3: Kartu mahasiswa tidak aktif")
print("mahasiswa terdaftar: True")
print("kartu aktif: False")
print("laboratorium buka: True")
print(cek_akses_laboratorium(True, False, True))
print("-"* 50)

print("case 4: Semua syarat tidak terpenuhi")
print("mahasiswa terdaftar: False")
print("kartu aktif: False")
print("laboratorium buka: False")
print( cek_akses_laboratorium(False, False, False))
print("-"* 50)

