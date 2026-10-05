def memenuhi_syarat(formulir, nilai, kehadiran, sanksi):
    return formulir and nilai >= 60 and kehadiran >= 75 and not sanksi

data = (True, 72, 80, False)
print("Dapat mengikuti praktikum:", memenuhi_syarat(*data))