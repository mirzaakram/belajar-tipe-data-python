# string sebaris
string_1 = "hello python"

text = "a multlline string/nin python"
print (text)

text = """a multlline string in python"""
print (text)

print ("+==========================================+")
print ("|            Biodata siswa                 | ")
print ("+==========================================+")
print ("|Nama \t\t : Mirza Akram                 |")
print ("|Nis \t\t : 123456789                   |")
print ("|Jurusan \t : Rekayasa perangkat lunak    |")
print ("|Umur \t\t : 15 Tahun                    |")
print ("|Hobi \t\t : Main game                   |")
print ("+==========================================+")

data = None
print(data)


Nama = "Mirza"
if Nama is None:
    print("nama belum diisi.")
else:
    print("Nama kamu adalah:",Nama)
    
list_1 = [2,4,8,16]
print(list_1[0])

list_2 = ["grayson","jason","tim","damian"]
print(list_2[2])

list_3 = [24,False,"Hello python"]
print(list_3[1])

#append
buah = ["sorento","dreamsccap"]
buah.append("california signature")
print(buah)

#extend
buah = ["aqua","tobacco"]
buah.extend(["out wod","pisang"])
print(buah)

#insert
angka = [1,2,3]
angka.insert(4,3)
print(angka)

#pop
buah = ["apel","jeruk","mangga","semangka","melon"]
buah.pop(2)
print(buah)

#sort
angka = [5,2,9,1]
angka.sort()
print(angka)

angka = [5,2,9,1]
angka.sort(reverse=True)
print(angka)

#clear
data = [5,6,7]
data.clear()
print(data)

#remove
buah = ["orange","merah","blue"]
buah.remove("orange")
print(buah)

#index
nama = ["ali","baka","gohan"]
print(nama.index("baka"))

#reverse
warna = ["merah","kuning","hijau"]
warna.reverse()
print(warna)

#count
angka = [4,4,4,5,5,5,5,6,6,6,7,7,7]
print(angka.count(4))

print("===program daftar belanja===")
print("-daging sapi")
print("-tomat")
print("-bumbu masak")
print("-kentang")
print("-sawi")
print("-daging ayam")

print("1.tambah barang")
barang = ["daging sapi","tomat","bumbu masak","kentang","daging ayam"]
barang.append("wortel")
print(barang)

print("2.hapus barang")
barang = ["daging sapi","tomat","bumbu masak","kentang","daging ayam"]
barang.remove("tomat")
print(barang)

print("3.lihat daftar")
barang = ["daging sapi","tomat","bumbu masak","kentang","daging ayam"]
barang.sort()
print(barang)

print("4.hapus semua")
barang = ["daging sapi","tomat","bumbu masak","kentang","sawi","daging ayam"]
barang.pop(4)
print(barang)

print("5.keluar")
data = ["daging sai","tomat","bumbu masak","kentang","sawi","daging ayam"]
data.clear()
print(data)

#tipe data tuple

tuple_1 = (2,3,4)
tuple_2 = ("giorno","jojo")
tuple_3 = (24, False, "Hallo")
print(tuple_1)

#fungsi tuple
alphabets = tuple("abcdefgh")
print(alphabets)

#list ke tuple

number = tuple([1,2,3,4])
print(number)

#range ke tuple

r = range(0,9)
rtuple = tuple(r)
print(rtuple)

#tipe data dictionary
biodata_1 = {
    "nama" : "mirza",
    "Hobi" : "game",
    "umur" : "15",
}
print("nama: %s" %(biodata_1["nama"]))
print("Hobi: %s" %(biodata_1["Hobi"]))
print("umur: %s" %(biodata_1["umur"]))