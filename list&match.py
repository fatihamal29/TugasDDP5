kendaraan = ["BG14564","Motor",1000,"Merah"]

kendaraan.append("2.000.000")
kendaraan.append(2)
kendaraan.insert(2,"Vario")
kendaraan.insert(3,"Honda")
print(kendaraan)

ket = '''Selamat Datang di Aplikasi Menghitung
masukan pilihan :
1. Untuk menghitung Luas Persegi
2. Untuk menghitung Luas Lingkaran
3. Untuk Menghitung Luas Segititga
'''
pilihan = input (ket)


match pilihan:
        case"1":
            print("Menghitung Luas Persegi")
            print("Rumus = Sisi x Sisi")
            sisi = int(input("Masukan Sisi :"))
            luasp = sisi * sisi
            print("hasil sisi =",luasp )
        case"2":
            print("Mengghitung Luas Lingkaran")
            print("Rumus = 3,14 x jari x jari")
            jari = float(input("Masukan Jari Jari :"))
            luasj = 3,14 * jari * jari
            print("hasil luas lingkaran",luasj)
        case"3":
            print("Menghitung Luas Segitiga")
            print("Rumus Segitiga : Alas x Tinggi")
            alas = int(input("Masukan Alas Segitiga : "))
            tinggi = int(input("Masukan Tinggi Segitiga :"))
            luast = 0,5*alas*tinggi
            print("hasil luas Segitiga :",luast)
        case _:
            print("salahhhh")