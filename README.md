# Pertemuan 11 - Dictionary/Map

Nama: Siti Fitriani 
NIM: 2225250213
Kelas: 3b


## Tujuan
Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value.

## Struktur Data
Key utama menggunakan NIM mahasiswa. Setiap value berisi nama, kelas, dan nilai.

## Struktur Folder
- `latihan/`: enam latihan dictionary.
- `praktik/`: program sistem data mahasiswa.

## Cara Menjalankan
Jalankan dari folder utama:

```bash
python praktik/data_mahasiswa.py
```

Untuk menjalankan latihan, contoh:

```bash
python latihan/01_dasar_dictionary.py
```

## Test Case
1. Pencarian A003: data Citra ditampilkan.
2. Pencarian A999: pesan `Data tidak ditemukan`.
3. Pembaruan A002: nilai berubah menjadi 82.
4. Penambahan A006: data Fajar berhasil ditambahkan.
5. Rekap: seluruh NIM dan data mahasiswa ditampilkan.

## Refleksi
Kesalahan yang dapat terjadi adalah `KeyError` ketika mengakses key yang tidak tersedia. Cara memperbaikinya adalah menggunakan `get()` atau memeriksa key menggunakan operator `in`.
