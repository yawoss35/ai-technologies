#apiler bozuk oldugu icin taslak olarak attım elime api gecerse kullanacagım

import requests
import os
import time

def temizle():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

print("Kullanmak istediğiniz yapay zekayı seçiniz..")
a = int(input("1- GPT3\n2- GPT4\n3- GPT5\n4- WormGPT\n>>"))
temizle()

if a == 1:
    c = input(">> ")
    url = f"https://dev-gpts.pantheonsite.io/wp-admin/js/apis/GPT-3.php?text={c}"
    req = requests.get(url)
    print(f"http status code: {req.status_code}")
    print(f"\n{req.text}")

elif a == 2:
    c = input(">> ")
    url = f"https://dev-gpts.pantheonsite.io/wp-admin/js/apis/GPT-4.php?text={c}"
    req = requests.get(url)
    print(f"http status code: {req.status_code}")
    print(f"\n{req.text}")

elif a == 3:
    c = input(">> ")
    url = f"https://dev-gpts.pantheonsite.io/wp-admin/js/apis/GPT-5.php?text={c}"
    req = requests.get(url)
    print(f"http status code: {req.status_code}")
    print(f"\n{req.text}")

elif a == 4:
    c = input(">> ")
    url = f"https://dev-gpts.pantheonsite.io/wp-admin/js/apis/WormGPT.php?text={c}"
    req = requests.get(url)
    print(f"http status code: {req.status_code}")
    print(f"\n{req.text}")

else:
    print("Bilinmeyen bir hata..")
