# Pertemuan 11 - Dictionary/Map

**Nama:** Aulia Rahma Ramadhani  
**NIM:** 2225250001  
**Kelas:** 3A

## Tujuan

Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value. Program ini digunakan untuk menyimpan, mencari, menambahkan, dan mengubah data mahasiswa, menampilkan seluruh data, serta menghitung rata-rata nilai menggunakan Python.

## Struktur Data

Program menggunakan dictionary `data_mahasiswa` untuk menyimpan data mahasiswa.

- **Key utama:** NIM mahasiswa, seperti `"A001"`, `"A002"`, dan `"A003"`.
- **Value:** Dictionary yang berisi nama mahasiswa, kelas, dan nilai.
- **Key pada value:** `"nama"`, `"kelas"`, dan `"nilai"`.

Contoh struktur data:

```python
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78}
}
```

Program menggunakan beberapa fungsi, yaitu `cari_mahasiswa()` untuk mencari data berdasarkan NIM, `tambah_mahasiswa()` untuk menambahkan data baru, `ubah_nilai()` untuk mengubah nilai, dan `rata_rata_nilai()` untuk menghitung rata-rata nilai mahasiswa.

## Cara Menjalankan

Program dijalankan melalui terminal pada folder utama repository.

```bash
python3 praktik/data_mahasiswa.py
```

Pada Windows, program juga dapat dijalankan menggunakan perintah:

```powershell
python praktik/data_mahasiswa.py
```

## Test Case

| No. | Input/Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | Mencari NIM `A003` | Data Citra ditemukan dengan kelas B dan nilai 92 | Data Citra ditampilkan | Lulus jika sesuai saat dijalankan |
| 2 | Mencari NIM `A999` | Muncul pesan data tidak ditemukan | Pesan data tidak ditemukan | Lulus jika sesuai saat dijalankan |
| 3 | Menambahkan mahasiswa `A006` dengan nama Fajar, kelas B, nilai 80 | Data mahasiswa baru berhasil ditambahkan | Pesan berhasil ditambahkan | Lulus jika sesuai saat dijalankan |
| 4 | Mengubah nilai NIM `A002` menjadi 82 | Nilai Budi berubah menjadi 82 | Rekap menampilkan nilai 82 | Lulus jika sesuai saat dijalankan |
| 5 | Menampilkan seluruh data dengan `items()` | Seluruh enam mahasiswa ditampilkan | Enam data mahasiswa ditampilkan | Lulus jika sesuai saat dijalankan |
| 6 | Menghitung rata-rata nilai setelah penambahan dan perubahan | Rata-rata nilai sebesar 83,50 | Rata-rata ditampilkan sebesar 83.50 | Lulus jika sesuai saat dijalankan |

*Catatan: Periksa hasil aktual dengan menjalankan program. Status pengujian ditetapkan setelah hasil terminal sesuai dengan hasil yang diharapkan.*

## Refleksi

Kesalahan akses key yang dapat terjadi adalah menggunakan `data_mahasiswa["A999"]` ketika NIM tersebut tidak tersedia. Kesalahan ini dapat menimbulkan `KeyError` karena key tidak ditemukan dalam dictionary. Cara memperbaikinya adalah menggunakan metode `get()`, misalnya `data_mahasiswa.get("A999")`, kemudian memeriksa apakah hasilnya `None` sebelum menampilkan data. Dengan cara tersebut, program dapat menangani NIM yang tidak ditemukan tanpa menyebabkan `KeyError`.