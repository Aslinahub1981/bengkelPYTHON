#!/usr/bin/env python
import random

# Senarai nama lagu
lagu = ["Ketipak ketipung Raya", "Raya Mana", "Alamak Raya Lagi ", "Raya kita Raya", "Jom pulang Raya"]

# Pilih lagu secara rawak
lagu_terpilih = random.choice(lagu)

# Buat fungsi untuk menentukan sama ada jawapan pengguna betul atau tidak
def semak_jawapan(jawapan, lagu_terpilih):
    if jawapan.lower() == lagu_terpilih.lower():
        return True
    else:
        return False

# Fungsi utama permainan
def main():
    tekaan_benar = False
    cubaan = 0
    
    print("Hai! Selamat datang ke permainan teka lagu!")
    print("Saya akan berikan anda beberapa cubaan untuk menebak lagu yang saya fikirkan.")
    print("Senarai lagu: ", lagu)
    
    while not tekaan_benar and cubaan < 3:
        jawapan = input("Cuba teka lagu yang saya fikirkan: ")
        cubaan += 1
        
        if semak_jawapan(jawapan, lagu_terpilih):
            print("Tahniah! Anda betul. Lagu yang saya fikirkan adalah:", lagu_terpilih)
            tekaan_benar = True
        else:
            print("Maaf, cuba lagi.")
    
    if not tekaan_benar:
        print("Maaf, anda telah melebihi jumlah cubaan yang dibenarkan. Lagu yang saya fikirkan adalah:", lagu_terpilih)
# Memanggil fungsi utama
if __name__ == "__main__":
    main()