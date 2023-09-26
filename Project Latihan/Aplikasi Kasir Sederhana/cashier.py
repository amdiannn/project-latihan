# buatlah program untuk menghitung total pembelian N buah barang dengan jumlah dan jumlah tertentu!

import os
os.system("cls")

# header
print("=" * 35)
print("\tToko Nusantara\t")
print("=" * 35)

# input user
harga = eval(input("Masukkan Harga Barang\t: Rp "))
jumlah = eval(input("Masukkan Jumlah Barang\t: "))

# view total harga
total = harga * jumlah
print(f"\nTotal Harga\t\t: Rp {total:,.2f}\n")

# input user 2
bayar = eval(input("Masukkan Jumlah Uang\t: Rp "))
kembalian = bayar - total

# view kembalian
print(f"Uang Kembalian\t\t: Rp {kembalian:,.2f}")