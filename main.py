import requests
import json
import time

class Renk:
    YESIL = '\033[92m'
    KIRMIZI = '\033[91m'
    CYAN = '\033[96m'
    SARI = '\033[93m'
    KALIN = '\033[1m'
    SIFIRLA = '\033[0m'

#YOUR API İS HERE (studio.google.com)
API_KEY = "API_HERE"

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

ornek_politika = """
Hizmet kalitesini artırmak için kullanıcıların uygulama içindeki tıklama alışkanlıklarını ve cihaz model bilgilerini kaydediyoruz. 
Konum bilgileriniz, yalnızca yerel içerikleri göstermek amacıyla siz izin verdiğiniz sürece kullanılır. 
Kişisel bilgileriniz üçüncü taraflara doğrudan satılmaz, ancak anonimleştirilmiş veriler istatistiksel analizler için kullanılabilir. 
Kullanıcılar istedikleri zaman veri paylaşımını ayarlar kısmından kısıtlayabilirler.
"""

komut = f"""
Sen uzman bir veri güvenliği avukatısın. Kullanıcıyı uyarmak için çıktını çok şatafatlı, bol emojili ve dikkat çekici bir formatta hazırla.

Şu kurallara KESİNLİKLE uy:
1. 🎯 RİSK SKORU: 1 ile 10 arası bir puan ver. Puanın yanına risk durumuna göre (🟢 Güvenli, 🟡 Dikkat, 🔴 Tehlike) emojilerinden birini koy.
2. 📝 KISA ÖZET: En kritik 3 maddeyi listele. Her maddenin başına o maddeyle uyumlu çarpıcı bir emoji (🚨, 👁️, 🕵️‍♂️, 📍 vb.) ekle.
3. Çıktı çok temiz, kolay okunabilir ve modern görünsün.

İncelenecek Metin: {ornek_politika}
"""

veri_paketi = {
    "contents": [{"parts": [{"text": komut}]}]
}
basliklar = {'Content-Type': 'application/json'}

print(f"\n{Renk.CYAN}{Renk.KALIN}🛡️ PrivacyGuard AI Başlatılıyor...{Renk.SIFIRLA}")
time.sleep(1)
print(f"{Renk.SARI}🔍 Gizlilik politikası taranıyor...{Renk.SIFIRLA}")
time.sleep(1.5)
print(f"{Renk.YESIL}⚙️ Yapay zeka analizi tamamlandı! Sonuçlar ekrana yansıtılıyor...\n{Renk.SIFIRLA}")
print(f"{Renk.KIRMIZI}{Renk.KALIN}{'-' * 50}{Renk.SIFIRLA}\n")

try:
    cevap = requests.post(url, headers=basliklar, data=json.dumps(veri_paketi))
    
    if cevap.status_code == 200:
        gelen_veri = cevap.json()
        ai_metni = gelen_veri['candidates'][0]['content']['parts'][0]['text']
        
       
        print(f"{Renk.KALIN}{ai_metni}{Renk.SIFIRLA}")
    else:
        print(f"{Renk.KIRMIZI}❌ Sunucu Hatası: {cevap.status_code}{Renk.SIFIRLA}")
        
except Exception as hata:
    print(f"{Renk.KIRMIZI}❌ Bir bağlantı hatası oluştu: {hata}{Renk.SIFIRLA}")

print(f"\n{Renk.KIRMIZI}{Renk.KALIN}{'-' * 50}{Renk.SIFIRLA}\n")