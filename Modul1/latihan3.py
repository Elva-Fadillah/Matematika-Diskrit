kehadiran =int(input("masukkan persentase kehadiran: "))
administrasi =input("apakah administrasi sudah lunas? (ya/tidak): ")
aktif =input("apakah mahasiswa aktif? (ya/tidak): ")
if kehadiran >= 75 and administrasi == "ya" and aktif == "ya":
    print("mahasiswa layak mengikuti ujian")
else:
    print("mahasiswa tidak layak mengikuti ujian")
