from fonksiyon import (konusma,dinleme,enter,dolar,euro,discord,bilgisayardaac,merhaba,nasilsin,youtube,youtubeac,netflix,saatkac,disney,google,tesekkurler,arastir,hesapmak,whatsapp,notdefteri,spotify,notal,notoku,notsil,sesazalt,sesarttir,kapat,kamera)


def switch(argument):
        argument2 = argument.split(" ")
        print(argument2)
        if "çirkin" or "tilki" in argument2:
                del argument2[0]
                argument = " ".join(map(str,argument2))

                print(argument)
                switcher = {
                        "merhaba": merhaba,

                        "nasılsın": nasilsin,
                        "napıyorsun": nasilsin,

                        "youtube": youtube,

                        "youtube'da aç": youtubeac,
                        "youtubeda aç": youtubeac,
                        "youtube'da ara": youtubeac,
                        "youtube ara": youtubeac,
                        "youtube aç": youtubeac,

                        "netflix": netflix,
                        "netflix aç": netflix,
                        "netflixi aç": netflix,

                        "saat kaç": saatkac,
                        "saati söyle": saatkac,

                        "disney": disney,
                        "disney aç": disney,
                        "disneyi aç": disney,

                        "google": google,
                        "google aç": google,

                        "teşekkürler": tesekkurler,
                        "teşekkür": tesekkurler,

                        "araştır": arastir,
                        "araştırma yap": arastir,

                        "hesap makinesi": hesapmak,
                        "hesap makinesini aç": hesapmak,

                        "whatsapp": whatsapp,
                        "whatsappı aç ": whatsapp,

                        "not defteri": notdefteri,

                        "spotify": spotify,

                        "not al": notal,
                        "dediklerimi not al": notal,

                        "not oku": notoku,
                        "notları oku": notoku,

                        "not sil": notsil,
                        "notları sil": notsil,

                        "ses azalt": sesazalt,
                        "ses kız": sesazalt,
                        "sesi azalt": sesazalt,
                        "sesi kıs": sesazalt,
                        "sesi kız": sesazalt,
                        "face kıs": sesazalt,
                        "face kız": sesazalt,

                        "ses arttır": sesarttir,
                        "sesi arttır": sesarttir,
                        "sesi çoğalt": sesarttir,
                        "ses ver": sesarttir,

                        "foto çek": kamera,
                        "fotoğraf çek": kamera,
                        "fotoğrafımı çek": kamera,
                        "fotomu çek": kamera,

                        "çek": enter,
                        "kek": enter,
                        "enter": enter,

                        "dolar": dolar,
                        "dolar kuru": dolar,
                        "dolar kuru kaç": dolar,
                        "dolar kaç": dolar,

                        "euro": euro,
                        "euro kuru": euro,
                        "euro kuru kaç": euro,
                        "euro kaç": euro,

                        "discord": discord,

                        "bilgisayarda aç":bilgisayardaac,
                        "bilgisayar'da aç": bilgisayardaac,
                        "uygulama aç": bilgisayardaac,
                        "program aç": bilgisayardaac,

                        "kapat": kapat,
                        "çık": kapat,
                        "kapa": kapat,
                        "kafa": kapat,
                        "kaba": kapat,
                        "kapağı": kapat,
                }
                func = switcher.get(argument, lambda:print("bulunamadı"));
                func();
print("başlatıldı........")

while True:
    ses = dinleme()
    print("dinleniyor")
    if bool(ses)==True:
            print(ses)
            ses = ses.lower()
            ses1 = str(ses)
            switch(ses)

