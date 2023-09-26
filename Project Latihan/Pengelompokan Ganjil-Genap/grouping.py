# buatlah program untuk menghitung banyaknya bilangan genap ataupun ganjil dari N buah bilangan yang diinput secara acak!

import os
os.system("cls")

# header
print("=" * 50)
print("\tMenghitung Banyaknya Bilangan\t")
print("=" * 50)

# input user
bilangan1 = int(input("Masukkan Bilangan Pertama\t: "))
bilangan2 = int(input("Masukkan Bilangan Kedua\t\t: "))

# view input value
list_bilangan = [i for i in range(bilangan1, bilangan2 + 1)]
print(f"\nDaftar Bilangan\t:\n{list_bilangan}\n")

# template output
genap = []
ganjil = []

# filtering
for angka in list_bilangan:
    if angka % 2 == 0:
        genap.append(angka)
    else:
        ganjil.append(angka)

# final output
print(f"Bilangan Genap\t:\n{', '.join([str(i) for i in genap])}\n")
print(f"Bilangan Ganjil\t:\n{', '.join([str(i) for i in ganjil])}")