# ============================================================
# ASESMEN MODUL 2 — Analisis Nomor Identitas
# Nama   : ELVA FADILLAH
# NIM    : 260306073
# Kelas  : 1A
# Tanggal:
# ============================================================

# -------------------------------------------------------
# Bagian 1: Tentukan ganjil/genap
# -------------------------------------------------------
def adalah_genap(n):
    return n % 2 == 0


# -------------------------------------------------------
# Bagian 2: Tentukan bilangan prima
# -------------------------------------------------------
def adalah_prima(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


# -------------------------------------------------------
# Bagian 3: FPB menggunakan algoritma Euclidean
# -------------------------------------------------------
def fpb(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# -------------------------------------------------------
# Bagian 4: KPK menggunakan FPB
# -------------------------------------------------------
def kpk(a, b):
    if a == 0 or b == 0:
        return 0
    return (a * b) // fpb(a, b)


# -------------------------------------------------------
# Bagian 5: Konversi desimal ke heksadesimal
# -------------------------------------------------------
def desimal_ke_hex(n):
    digit_hex = "0123456789ABCDEF"
    # Kasus batas: 0
    if n == 0:
        return "0"
    hasil = ""
    # Pembagian berulang dengan 16, sisa bagi dibaca dari bawah ke atas
    while n > 0:
        sisa = n % 16
        hasil = digit_hex[sisa] + hasil   # tempel di depan
        n = n // 16
    return hasil


# -------------------------------------------------------
# Data perangkat (nomor identitas)
# -------------------------------------------------------
perangkat = [
    {"nama": "Router-01",  "id": 97},
    {"nama": "Switch-02",  "id": 84},
    {"nama": "Server-03",  "id": 100},
    {"nama": "PC-Lab-04",  "id": 17},
    {"nama": "Printer-05", "id": 60},
    {"nama": "AP-Wifi-06", "id": 37},
]

# Pasangan perangkat untuk analisis FPB/KPK
pasangan_maintenance = [
    ("Router-01", 97, "Switch-02",  84),
    ("Server-03", 100, "PC-Lab-04", 60),
]


# -------------------------------------------------------
# Tampilkan hasil analisis
# -------------------------------------------------------
def analisis_perangkat(perangkat):
    print("=" * 65)
    print(f"{'Nama':<14} {'ID':>5} {'Genap?':>7} {'Prima?':>7} {'Hex':>8}")
    print("=" * 65)
    for p in perangkat:
        nama = p["nama"]
        n    = p["id"]
        genap = adalah_genap(n)
        prima = adalah_prima(n)
        hex_n = desimal_ke_hex(n)
        print(f"{nama:<14} {n:>5} {str(genap):>7} {str(prima):>7} {str(hex_n):>8}")
    print()

def analisis_maintenance(pasangan):
    print("Jadwal Maintenance Bersama:")
    print("-" * 45)
    for nama_a, id_a, nama_b, id_b in pasangan:
        hasil_fpb = fpb(id_a, id_b)
        hasil_kpk = kpk(id_a, id_b)
        print(f"  {nama_a} (ID={id_a}) & {nama_b} (ID={id_b})")
        print(f"    FPB = {hasil_fpb} | KPK = {hasil_kpk}")
        print()


# Jalankan
analisis_perangkat(perangkat)
analisis_maintenance(pasangan_maintenance)