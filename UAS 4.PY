UNKRIS = {
    "141401081": "Rifaldi Maulana",
    "141401041": "Rafi Yanda",
    "141401044": "Sandi Irawan",
    # Add more students here
}

kehadiran = {}
 
def tandai_kehadiran(nim):
    if nim in UNKRIS:
        if nim in kehadiran:
            print("Kehadiran siswa ini sudah ditandai.")
        else:
            kehadiran[nim] = "Hadir"
            print("Kehadiran ditandai untuk",UNKRIS[nim])
    else:
       print("Siswa dengan NIM", nim, "tidak ditemukan.")

while True:
    nim = input("Masukkan NIM Mahasiswa : ")
    if nim.lower() == "Tidak Haadir":
        break
    tandai_kehadiran(nim)

print("\nKehadiran Siswa :")
for UNKRIS in kehadiran:
    print(f"{UNKRIS[UNKRIS]} - {kehadiran[UNKRIS]}")

#1. **Data Mahasiswa (`UNKRIS`)**:
   #- `UNKRIS` adalah sebuah kamus (dictionary) yang menyimpan informasi mahasiswa UNKRIS.
   #- Setiap elemen kamus memiliki format `"NIM": "Nama Mahasiswa"`, di mana NIM (Nomor Induk Mahasiswa) adalah kunci, dan nama mahasiswa adalah nilai.

#2. **Daftar Kehadiran (`kehadiran`)**:
    #- `kehadiran` adalah sebuah kamus yang digunakan untuk menyimpan informasi kehadiran mahasiswa.
   #- Setiap elemen kamus memiliki format `"NIM": "Status Kehadiran"`, di mana NIM adalah kunci, dan status kehadiran (misalnya, "Hadir") adalah nilai.

#3. **Fungsi `tandai_kehadiran`**:
   #- Fungsi ini digunakan untuk menandai kehadiran mahasiswa berdasarkan NIM yang dimasukkan.
  # - Jika NIM valid (ada dalam kamus `UNKRIS`), dan kehadiran belum ditandai sebelumnya, maka kehadiran mahasiswa akan dicatat.
   #- Jika NIM sudah ada dalam daftar kehadiran, pesan akan dicetak bahwa kehadiran sudah ditandai sebelumnya.
   #- Jika NIM tidak ditemukan dalam data mahasiswa, pesan akan dicetak bahwa siswa tidak ditemukan.

#4. **Loop Input (`while True`)**:
   #- Program menggunakan loop tak terbatas (`while True`) untuk terus menerima input NIM dari pengguna.
   #- Pengguna dapat memasukkan NIM mahasiswa atau mengetik "Tidak Haadir" untuk keluar dari loop dan mengakhiri program.

#5. **Cetak Daftar Kehadiran**:
  # - Setelah loop input berakhir, program mencetak daftar kehadiran mahasiswa.
  # - Menggunakan loop `for` untuk mengakses setiap NIM dalam kamus `kehadiran` dan mencetak NIM beserta status kehadiran.

