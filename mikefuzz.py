import requests
urll=input("fuzzing yapılacak site url giriniz: ")
wordlist=input("wordlist dosyasını giriniz: ")
dosya=open(wordlist,"r")
icerik=dosya.read()
dosya.close()
header={"Cookie": "security=low; PHPSESSID=a0b29e43b154e8cf261c3a93686bdd94"}
for i in icerik.split("\n"):
    print(i)
    url=urll+str(i)
    sonuc=requests.get(url=url)
    if "200" in str(sonuc.status_code):
        print("bulunan dizinler; ",i)
