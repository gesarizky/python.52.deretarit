# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# Menginput
a = int(input("Masukan Nilai Awal Deret (a) : "))
b = int(input("Masukan Nilai Rasio Deret (b): "))
n = int(input("Masukan Nilai Deret (n): "))

# Mengkonversi
un =  a + ((n - 1) * b)
sn = n / 2 * (2 * a + ((n - 1) * b))


# Menampilkan Hasil
print('==========================================================')
print('Maka Nilai Suku Ke ',n,'=',un)
print('Maka Nilai Penjumlahan Deret =',sn)
print('==========================================================')
