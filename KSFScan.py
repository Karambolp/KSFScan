import requests



def guvenlik_duvari_tespit(url):
    try:
        response = requests.get(url)

        # Sunucu tarafından sağlanan güvenlik başlıklarını kontrol et
        guvenlik_basliklari = response.headers.get("Server")

        if guvenlik_basliklari:
            print(f"Website Güvenlik Duvarı: {guvenlik_basliklari}")
        else:
            print("Güvenlik duvarı tespit edilemedi.")

    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    print("KSFScan Aracına Hoşgeldiniz")
    print("-----------------------------")

    # Kullanıcıdan sorgulanacak web sitesi URL'sini al
    hedef_url = input("Güvenlik duvarını tespit etmek için web sitesi URL'sini Https dahil olmak üzere giriniz: ")

    # Güvenlik duvarını tespit et
    guvenlik_duvari_tespit(hedef_url)

