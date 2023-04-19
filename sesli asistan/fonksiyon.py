import random
import pyaudio
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import pyautogui
import os
import datetime
from datetime import datetime
import time
import webbrowser
import requests
from bs4 import BeautifulSoup
kayit = sr.Recognizer()
pyautogui.FAILSAFE = False
emir =["emredersiniz","emrin olur","hemen ","sen iste yeterki","tamamdır","bende bu iş","paşa gönlün ne isterse","tamam"]

def konusma(metin):
    tts =gTTS(text=metin,lang="tr",slow=False)
    ses= "konusma1.mp3"
    tts.save(ses)
    playsound("konusma1.mp3")
    os.remove(ses)

def dinleme(a=False):
    with sr.Microphone() as kaynak:
        print("dinleniyor")
        if a:
            print(a)
        mikrofon = kayit.listen(kaynak)
        ses = ""
        try:
            ses = kayit.recognize_google(mikrofon, language="tr-TR")
        except sr.UnknownValueError:
            print("asistan:anlayamadım")
        except sr.RequestError:
            print("sistem bozukk")
        return ses
def asistan():
    print("seni duydum")
def merhaba():
    print("merhaba")
    mrhb = ["sanada merhaba harika insan", "merhaba developer", "merhaba emre", "merhaba efendim"]
    konusma(random.choice(mrhb))
def nasilsin():
    nslsn = ["iyiyim", "harikayım", "çok güzel bir gün", "iyi bro", "muhteşem"]
    konusma(random.choice(nslsn))
def youtube():
    konusma(random.choice(emir))
    url = 'www.youtube.com'
    webbrowser.get().open(url)
def youtubeac():
    konusma('ne açmamı istiyorsunuz')
    ses2 = dinleme()
    url = 'https://www.youtube.com/results?search_query=' + ses2
    webbrowser.get().open(url)
    konusma(ses2 + ' için bulduklarım')
def netflix():
    konusma(random.choice(emir))
    pyautogui.press('win')
    pyautogui.typewrite("netflix")
    pyautogui.press('enter')
def saatkac():
    konusma(datetime.now().strftime('%H:%M:%S'))
def disney():
    konusma(random.choice(emir))
    pyautogui.press('win')
    pyautogui.typewrite("disney")
    pyautogui.press('enter')
def google():
    konusma(random.choice(emir))
    url = 'www.google.com'
    webbrowser.get().open(url)
def tesekkurler():
    tesekkur = ["her zaman", "birşey değil", "senin için varım"]
    konusma(random.choice(tesekkur))
def arastir():
    konusma('ne aramak istiyorsunuz')
    ses2 = dinleme()
    url = 'https://www.google.com/search?q=' + ses2
    webbrowser.get().open(url)
    konusma(ses2 + ' için bulduklarım')
def hesapmak():
    konusma(random.choice(emir))
    pyautogui.press('win')
    pyautogui.typewrite("hesap makinesi")
    pyautogui.press('enter')
def whatsapp():
    konusma(random.choice(emir))
    pyautogui.press('win')
    pyautogui.typewrite("whatsapp")
    pyautogui.press('enter')
def notdefteri():
    konusma(random.choice(emir))
    pyautogui.press('win')
    pyautogui.typewrite("not defteri")
    pyautogui.press('enter')
def spotify():
    konusma(random.choice(emir))
    pyautogui.press('win')
    pyautogui.typewrite("spotify")
    pyautogui.press('enter')
def bilgisayardaac():
    konusma(random.choice(emir))
    konusma('ne açmak istiyorsunuz')
    ses2 = dinleme()
    sesstr = str(ses2)
    pyautogui.press('win')
    pyautogui.typewrite(sesstr)
    pyautogui.press('enter')

def discord():
    konusma(random.choice(emir))
    os.startfile(r'C:\Users\emre\AppData\Local\Discord\app-1.0.9012\Discord.exe')

def notal():
    konusma("Evet sizi dinliyorum")
    file1 = open("not.txt", "a")
    note = dinleme()
    file1.write(note + "\n")
    file1.close()
    konusma("Notunuzu yazdım.")
def notoku():
    print("not okunuyor")
    file1 = open("not.txt", "r")
    abc = file1.read()
    print(file1.read())
    konusma(abc)
    file1.close()
    konusma("Notlarınızı okudum")
def notsil():
    konusma("Notlarınızı silmek istediğinizden emin misiniz?")
    ses2 = dinleme()
    if "evet" or "evet sil" in ses2:
        file1 = open("not.txt", "r+")
        file1.truncate(0)
        konusma("Notlarınız başarıyla silindi.")

    if "hayır" or "hayır kalsın" or "hayır silme" in ses2:
        konusma("Notlarınız silinmeyecek.")
def sesazalt():
    konusma(random.choice(emir))
    for i in range(5):
        pyautogui.press('volumedown')
def sesarttir():
    konusma(random.choice(emir))
    for i in range(5):
        pyautogui.press('volumeup')
def kamera():
    konusma(random.choice(emir))
    pyautogui.press('win')
    pyautogui.typewrite("kamera")
    time.sleep(3)
    pyautogui.press('enter')
def enter():
    pyautogui.press('enter')
def dolar():
    url1 = "https://www.google.com/finance/quote/USD-TRY?hl=tr"
    sayfa = requests.get(url1)
    htmlsayfa = BeautifulSoup(sayfa.content,"html.parser")
    dolar = htmlsayfa.find("div",class_="YMlKec fxKbKc").get_text()
    print(dolar)
    dolar1 = "dolar kuru"+str(dolar[:5])
    konusma(dolar1)
def euro():
    url1 = "https://www.google.com/finance/quote/EUR-TRY?hl=tr"
    sayfa = requests.get(url1)
    htmlsayfa = BeautifulSoup(sayfa.content,"html.parser")
    euro = htmlsayfa.find("div",class_="YMlKec fxKbKc").get_text()
    print(euro)
    euro1 = "euro kuru"+str(euro[:5])
    konusma(euro1)

def kapat():
    konusma("çıkış yapılıyor")
    quit()

