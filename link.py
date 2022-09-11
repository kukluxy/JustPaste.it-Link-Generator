import time
import string
import random
from colorama import Fore, init
import requests
import ctypes

iyi = 0
kotu = 0
kontrol = 0
toplam = 0

ctypes.windll.kernel32.SetConsoleTitleW(f"JustPaste.it Link Bulucu")

init(autoreset=True)

print(Fore.CYAN+"""

       JustPaste.it Link Bulucu v3.1 xd                       

                        """)

print(Fore.GREEN + "Seciniz:")
print(Fore.LIGHTGREEN_EX + "[1] Link Oluştur / Kontrol Et = 1'e basınız")
select = int(input("\n> "))

while select <= 0:
    print(Fore.RED + "Gecersiz Sayi.")
    select = int(input("\n> "))

while select > 2:
    print(Fore.RED + "Gecersiz Sayi.")
    select = int(input("\n> "))


if select == 1:
    print(Fore.LIGHTCYAN_EX + "\nKac Tane Link Olusturulsun ?\n")
    q = int(input("> "))
    while q <= 0:
        print(Fore.RED + "Incorrect value.")
        print(Fore.LIGHTCYAN_EX + "\nKac Tane Link Olusturulsun ?\n")
        q = int(input("> "))

    total = q


    for g in range(q):
        links = ""
        links = "".join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.digits) for r in range(5))

        headers = {
                'Host': 'justpaste.it',
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
                "Accept-Language": "fr,en-US;q=0.9,en;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                'Connection': 'keep-alive'
            }


        sess = requests.Session()
        url= f"https://justpaste.it/{links}"
    
        req= sess.get(url, headers = headers)
        if req.status_code == 200:
            iyi = iyi + 1
            kontrol = kontrol + 1
            print(Fore.YELLOW + url)
            print(Fore.LIGHTGREEN_EX + "[+] " + Fore.MAGENTA + ">>" + Fore.LIGHTYELLOW_EX + " Link Bulundu" + "\n")
            ctypes.windll.kernel32.SetConsoleTitleW(f"JustPaste.it Link Bulucu | İyi: {iyi} | kotu: {kotu} | kontrol: {kontrol}/{toplam} | ")
            with open ("linkler.txt", "a") as results:
                results.write(f"https://justpaste.it/{links}" + "\n")

        elif req.status_code == 404:
            kotu = kotu + 1
            kontrol = kontrol + 1
            print(Fore.YELLOW + url)
            print(Fore.LIGHTRED_EX+ "[-] " + Fore.MAGENTA + ">>" + Fore.LIGHTYELLOW_EX + " Link Gecersiz" + "\n")
            ctypes.windll.kernel32.SetConsoleTitleW(f"JustPaste.it Link Bulucu | iyi: {iyi} | kotu: {kotu} | kontrol: {kontrol}/{toplam} | ")

            
print(Fore.CYAN + "Linkler Kaydedildi Hocam - " + Fore.LIGHTGREEN_EX + str(iyi) + Fore.CYAN + " iyi / " + Fore.LIGHTRED_EX + str(kotu) +  Fore.CYAN + " gecersiz...")
time.sleep(2)