# Disini saya akan menjelaskan cara membuat program sederhana menghitung nilai akhir mahasiswa mengunakan bahasa program python. pada program sederhana ini yang pertama kita harus menentukan ketentuan soal yang diberikan yaitu membuat data mahasiswa dan menghitung nilai akhir mahasiswa:
# nilai keperibadian= 15/100
# nilai tugas= 15/100
# nilai uts 30/100
# nilai uas40/100
# A = 80–100
# B = 70–79
# C = 60 -69
# D  = 50–59
# E = 0–49/masukan nilai lebih dari 100

print("Menghitung nilai akhir mahasiswa")
print("===========================")
nama = input("\nMasukan Nama :")
kep = float(input("masukan nilai keperibadian :"))
tugas = float(input("masukan nilai tugas :"))
uts = float(input("masukan nilai UTS :"))
uas = float(input("masukan nilai UAS :"))

na = (15/100 * kep) + (15/100 * tugas) + (30/100 * uas) + (40/100 * uas)
if na <= 100 and na >=79:
    nf = 'A'
elif na <= 80 and na >=69:
    nf = 'B'
elif na <= 70 and na >=59:
    nf = 'C'
elif na <= 60 and na >=49:
    nf = 'D'
else:
    nf = 'E'
print("===========================")
print("\nNama :", nama)
print("Nilai Akir = %0.2f" % na)
print("Nilai Huruf = %c" % nf)