import requests
import sys

# AZ ÖNCE KOPYALADIĞIN RAW LİNKİNİ BURAYA YAPIŞTIR
GUNCEL_KOD_URL = "https://raw.githubusercontent.com/Willton0/sweet-project/refs/heads/main/main.py"

def hileyi_calistir():
    try:
        print("[*] SWEET Bulut Sistemi Baglaniyor...")
        # İnternetten güncel kodu çekiyoruz
        response = requests.get(GUNCEL_KOD_URL)
        
        if response.status_code == 200:
            print("[+] Guncelleme Basarili! Hile baslatiliyor...")
            # İndirilen kodu bellekte çalıştırır
            exec(response.text, globals()) 
        else:
            print("[-] Kod cekilemedi! Sunucu hatasi.")
    except Exception as e:
        print(f"[-] Kritik Hata: {e}")
        input("Kapatmak icin Enter'a bas...")

if __name__ == "__main__":
    hileyi_calistir()