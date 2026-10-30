def cari_mahasiswa(data, nim):
    return data.get(nim)


mahasiswa = {
    "A001": {"nama": "Ayu", "nilai": 85},
    "A002": {"nama": "Budi", "nilai": 78}
}

hasil = cari_mahasiswa(mahasiswa, "A002")
print(hasil)

hasil = cari_mahasiswa(mahasiswa, "A003")
if hasil is None:
    print("Data tidak ditemukan")
else:
    print(hasil)
