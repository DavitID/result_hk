# CODE BY VID ID

# IMPORT
import re, sys, os

try:
  import requests
  from bs4 import BeautifulSoup as bs
except ImportError:
  os.system("pip install requests")
  os.system("pip install bs4")
  os.system("python pool.py")

# WARNA
merah = "\033[1;31m"
biru = "\033[1;34m"
kuning = "\033[1;33m"
putih = "\033[1;37m"
hijau = "\033[1;32m"
normal = "\033[0m"
banred = "\033[0;41m"
cyan = "\033[1;36m"
biru = "\033[1;34m"

# URL UNTUK DI SCRAP
url = "https://hkpools1.net/"

# CLEAR
def clear():
  os.system("cls" if os.name == "nt" else "clear")

# POOL 1
def pool1():
  req = requests.get(url)
  soup = bs(req.content, "html.parser")
  pool = soup.findAll("span", class_="ball-1")

  regex = re.findall("[0-9]+", str(pool))
  print(f"{kuning}Reward [1]{biru}: {putih}"+regex[1], regex[3], regex[5], regex[7], regex[9], regex[11])

# POOL 2
def pool2():
  req = requests.get(url)
  soup = bs(req.content, "html.parser")
  pool = soup.findAll("span", class_="ball-2")

  regex = re.findall("[0-9]+", str(pool))
  print(f"{kuning}Reward [2]{biru}: {putih}"+regex[1], regex[3], regex[5], regex[7], regex[9], regex[11])

# POOL 3
def pool3():
  req = requests.get(url)
  soup = bs(req.content, "html.parser")
  pool = soup.findAll("span", class_="ball-3")

  regex = re.findall("[0-9]+", str(pool))
  print(f"{kuning}Reward [3]{biru}: {putih}"+regex[1], regex[3], regex[5], regex[7], regex[9], regex[11])

# BANNER
def banner():
  print(f"""
{biru}  __________            
 ///////////\                 
///////////  \      {cyan}LIVEDRAW HKPOOL
{putih}|    {merah}_    {putih}|  |
{putih}|{kuning}[] {merah}| | {kuning}[]{putih}|{kuning}[]{putih}|           {banred}VIT ID{normal}
{putih}|   {merah}| |   {putih}|  |
{hijau}##############

""")

if __name__ == "__main__":
  clear()
  try:
    banner()
    print(f"{putih}----------{cyan}=={hijau}[{banred}RESULT DRAW{normal}{hijau}]{cyan}=={putih}----------{normal}\n")
    pool1()
    pool2()
    pool3()
  except ConnectionError:
    exit(f"{banred}CHECK YOUR NETWORK{normal}")
