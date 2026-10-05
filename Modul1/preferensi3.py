python = {"Ani", "Budi", "Citra"}
java = {"Budi", "Deni"}
sql = {"Ani", "Deni", "Eka"}
semua_mahasiswa = {"Ani", "Budi", "Citra", "Deni", "Eka", "Fajar"}

print("---------------------------------------------------------")

python_saja = python - (java | sql)
python_dan_java = python & java
minimal_satu = python | java | sql
tidak_ketiganya = semua_mahasiswa - (python | java | sql)

print("Pyhton saja:", python_saja)
print("Python dan java:", python_dan_java)
print("Minimal satu teknologi:", minimal_satu)
print("Tidak menyukai ketiganya:", tidak_ketiganya)