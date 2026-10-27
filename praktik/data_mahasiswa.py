
# Praktik Pertemuan 11 - Sistem Data Mahasiswa

def cari_mahasiswa(data, nim):
    """Mencari data mahasiswa berdasarkan NIM."""
    return data.get(nim)


def tambah_mahasiswa(data, nim, nama, kelas, nilai):
    """Menambahkan data mahasiswa baru."""
    if nim in data:
        return False

    data[nim] = {
        "nama": nama,
        "kelas": kelas,
        "nilai": nilai
    }
    return True


def ubah_nilai(data, nim, nilai_baru):
    """Mengubah nilai mahasiswa berdasarkan NIM."""
    if nim not in data:
        return False

    data[nim]["nilai"] = nilai_baru
    return True


def rata_rata_nilai(data):
    """Menghitung rata-rata nilai seluruh mahasiswa."""
    if len(data) == 0:
        return 0

    total = 0
    for mahasiswa in data.values():
        total += mahasiswa["nilai"]

    return total / len(data)


data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

# 1. Mencari mahasiswa berdasarkan NIM
print("=== PENCARIAN MAHASISWA ===")

nim_dicari = "A003"
hasil = cari_mahasiswa(data_mahasiswa, nim_dicari)

if hasil is not None:
    print(f"NIM: {nim_dicari}")
    print(f"Nama: {hasil['nama']}")
    print(f"Kelas: {hasil['kelas']}")
    print(f"Nilai: {hasil['nilai']}")
else:
    print("Data mahasiswa tidak ditemukan.")

# 2. Menguji NIM yang tidak tersedia
print("\n=== PENCARIAN NIM TIDAK TERSEDIA ===")

nim_dicari = "A999"
hasil = cari_mahasiswa(data_mahasiswa, nim_dicari)

if hasil is None:
    print(f"NIM {nim_dicari}: Data tidak ditemukan.")
else:
    print(hasil)

# 3. Menambahkan mahasiswa baru
print("\n=== TAMBAH MAHASISWA ===")

berhasil = tambah_mahasiswa(
    data_mahasiswa, "A006", "Fajar", "B", 80
)

if berhasil:
    print("Mahasiswa A006 berhasil ditambahkan.")
else:
    print("NIM sudah terdaftar.")

# 4. Mengubah nilai mahasiswa
print("\n=== UBAH NILAI ===")

berhasil = ubah_nilai(data_mahasiswa, "A002", 82)

if berhasil:
    print("Nilai Budi berhasil diubah menjadi 82.")
else:
    print("Data mahasiswa tidak ditemukan.")

# 5. Menampilkan seluruh data menggunakan items()
print("\n=== SELURUH DATA MAHASISWA ===")

for nim, info in data_mahasiswa.items():
    print(
        f"{nim} | {info['nama']} | "
        f"Kelas {info['kelas']} | Nilai {info['nilai']}"
    )

# 6. Menghitung rata-rata nilai
print("\n=== RATA-RATA NILAI ===")
print(f"Rata-rata nilai: {rata_rata_nilai(data_mahasiswa):.2f}")
