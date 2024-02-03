# kalkulator sederhana
print(20*"=")
print("Kalkulator Sederhana")
print(20*"=" + "\n")

angka_1 = float(input("masukan angka 1 = "))
operator = input("operator (+,-,x,/) : ")
angka_2 = float(input("masukan angka 2 = "))

# percabangannya
# pernyataan if digunakan untuk membuat suatu kondisi atau percabangan. Ini memungkinkan program untuk menjalankan serangkaian pernyataan tertentu jika suatu kondisi tertentu terpenuhi atau benar. Berikut adalah struktur dasar dari pernyataan if:
# Pernyataan elif Ini memungkinkan program untuk mengevaluasi kondisi secara berturut-turut dan menjalankan blok kode yang sesuai dari kondisi pertama yang terpenuhi. Berikut adalah struktur dasar dari pernyataan elif:
# float adalah tipe data yang digunakan untuk merepresentasikan bilangan desimal atau floating-point.

if operator == "+":
	hasil = angka_1 + angka_2
	print(f"hasilnya adalah {hasil}")
elif operator == "-":
	hasil = angka_1 - angka_2
	print(f"hasilnya adalah {hasil}")
elif operator == "x" or operator == "*":
	hasil = angka_1 * angka_2
	print(f"hasilnya adalah {hasil}")
elif operator == "/":
	hasil = angka_1 / angka_2
	print(f"hasilnya adalah {hasil}")
else:
	print("masukan yang bener dong!, aku pusying")

print("Akhir dari program, terima gajih!")