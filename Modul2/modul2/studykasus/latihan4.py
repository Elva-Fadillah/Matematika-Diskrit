def desimal_ke_biner(n):
    if n == 0:
        return "0"
    hasil = ""
    while n > 0:
        hasil = str(n % 2) + hasil
        n //= 2
    return hasil

def desimal_ke_oktal(n):
    if n == 0:
        return "0"
    hasil = ""
    while n > 0:
        hasil = str(n % 8) + hasil
        n //= 8
    return hasil

def desimal_ke_hex(n):
    digit_hex = "0123456789ABCDEF"
    if n == 0:
        return "0"
    hasil = ""
    while n > 0:
        hasil = digit_hex[n % 16] + hasil
        n //= 16
    return hasil


id_input = int(input("Masukkan ID perangkat: "))

print(f"{'Desimal':>8} {'Biner':>12} {'Oktal':>8} {'Heksadesimal':>14}")
print("=" * 45)
print(f"{id_input:>8} {desimal_ke_biner(id_input):>12} {desimal_ke_oktal(id_input):>8} {desimal_ke_hex(id_input):>14}")

print("\nVerifikasi menggunakan fungsi bawaan Python:")
print(f"  bin={bin(id_input)}, oct={oct(id_input)}, hex={hex(id_input).upper()}")