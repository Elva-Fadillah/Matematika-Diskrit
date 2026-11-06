def fpb(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def kpk(a, b):
    return abs(a * b) // fpb(a, b)

def jadwal_backup(interval_a, interval_b, durasi_pantau=120):
    """
    Menentukan jadwal backup bersama dua server.
    Menampilkan semua momen backup dalam rentang durasi pantau.
    """
    waktu_bersama = kpk(interval_a, interval_b)

    # Buat jadwal backup masing-masing server
    jadwal_a = set(range(0, durasi_pantau + 1, interval_a))
    jadwal_b = set(range(0, durasi_pantau + 1, interval_b))

    # Momen backup bersamaan
    bersamaan = sorted(jadwal_a & jadwal_b)

    print(f"Server A: backup setiap {interval_a} menit")
    print(f"Server B: backup setiap {interval_b} menit")
    print()
    print(f"FPB({interval_a}, {interval_b}) = {fpb(interval_a, interval_b)}")
    print(f"KPK({interval_a}, {interval_b}) = {waktu_bersama}")
    print()
    print(f"Pertama kali backup bersamaan: menit ke-{waktu_bersama}")
    print()
    print(f"Jadwal backup bersamaan dalam {durasi_pantau} menit ke depan:")
    print(bersamaan)

# Kasus utama: Server A = 12 menit, Server B = 18 menit
jadwal_backup(12, 18)

print()
print("=" * 50)
print()

# Kasus tambahan: Server C = 15 menit, Server D = 20 menit
jadwal_backup(15, 20)
def adalah_prima(n):
    if n <= 1:
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

def periksa_id_perangkat(daftar_id):
    print("\nVerifikasi ID Perangkat:")
    print(f"{'ID':>8} {'Prima?':>8} {'Keterangan'}")
    print("-" * 35)
    for id_perangkat in daftar_id:
        status = adalah_prima(id_perangkat)
        ket = "Dapat digunakan sebagai kunci" if status else "Bukan bilangan prima"
        print(f"{id_perangkat:>8} {str(status):>8}  {ket}")

daftar_id_uji = [7, 11, 15, 23, 49, 97, 100, 101]
periksa_id_perangkat(daftar_id_uji)