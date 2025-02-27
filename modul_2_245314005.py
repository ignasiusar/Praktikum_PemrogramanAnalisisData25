#Ignatius Aryajulio P.
#modul 2_ tugas Baru * Basics Py
#ver 1.0

#py program untuk memasukkan input user nama dan alamat

nama = input("Halo, siapa nama mu? : ")
print(f"Hallo, {nama}!")

alamat = input(f"Halo, {nama}! Alamat rumahmu di mana? ")
print(f"Oke, {nama}, jadi alamat rumahmu di {alamat}")

#Q2 input angka
x= input("Masukkan satu angka dong : ")
y=3
z="2"

print(int(x) + y)
print(int(x) + y)
print(int(x) * y)
print(int(x) * y)
print(int(x) + int(z))
print(int(x + z))
print(int(x) + int(z))
print(int(x) * int(z))

#Q3 Masukkan Panjang dan Lebar Ruangan
panjang = float(input("Masukkan Panjang Ruangannya Dong : "))
Lebar = float(input("Masukkan Lebar Ruangannya dong  : "))
luas =  panjang * Lebar 
print(f"Maka Luas Ruangan Mu Adalah  : {luas}")

#Q4 Hitung Umur Tahun Depan
Name = input("Masukkan Nama User disini ya : ")
umur = int(input("Masukkan Umur User Disini ya : "))
umurTahunDepan = umur + 1
print(f"Halo, {Name}! jadi Tahun Depan Umur mu adalah {umurTahunDepan}, Selamat Tambah Tua ya!")

#Q5 Hitung Hitungan Aritmatika
a= 7 + 3 * 5
b= 5.5 * 6 // 2 + 8
c= -3 ** 2
d= 50 * 2 + (60 - 20) / 4
print(f"Hasil Perhitungan A = {a}, \n Hasil Perhitungan B = {b}, \n Hasil Perhitungan C ={c} \n Hasil Perhitungan D = {d}")

#Q6 Jumlah Kedua Bilangan 
bil1 = float(input("Masukkan bilangan pertama: "))
bil2 = float(input("Masukkan bilangan kedua: "))
print("Jumlah kedua bilangan: ", bil1 + bil2)

#Q7 Hitung BMI
berat = int(input("Masukkan Berat Badan Mu : "))
tinggi= int(input("Masukkan Tinggi Mu: "))
namaa = input("Masukkan Nama Mu : ")
bmi = berat / (tinggi **2)
print(f" Halo, {namaa}! jadi berat mu {berat} kg, dan tinggi mu {tinggi} cm. Jadi BMI mu adalah: {bmi}")

#Q8 Hitung Pensiun
from datetime import datetime

tahunSekarang = datetime.now().year
usiaSekarang = int(input("Masukkan Usia Mu Sekarang Dong : "))
usiaPensiun = int(input("Kira Kira kamu mau pensiun umur berapa ? : "))
namamu = input("Nama Kamu Siapa ? : ")
sisaTahun = usiaPensiun - usiaSekarang
tahunPensiun = tahunSekarang + sisaTahun
print(f"Halo, {namamu}! jadi kamu akan pensiun di tahun {tahunPensiun} yaitu {sisaTahun} tahun dari sekarang")


