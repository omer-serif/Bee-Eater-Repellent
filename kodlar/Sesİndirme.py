from selenium import webdriver
from bs4 import BeautifulSoup
import time
#Bu ses indirme farklı bir siteden ve tüm sınıfları tek tek indiriyor.

trler=0
driver = webdriver.Chrome()
url = "https://xeno-canto.org/explore?query=%20bee-eater"
driver.get(url)
time.sleep(5)
sayfa=1

#ArıKuşu
for i in range(57):
    html = driver.page_source
    html = BeautifulSoup(html, "html.parser")
    while trler < 30:

        link = html.find("body").find("table", class_="results").find("tbody").find_all("tr")[trler].find_all("td")[11]
        link = link.find("a")
        link = link.get("href")
        driver.get(link)

        print(trler, ".indirme işlemi tamamlandı")
        trler += 1
    trler=0
    sayfa+=1
    sonraki = "https://xeno-canto.org/explore?query=+bee-eater&pg="+str(sayfa)
    driver.get(sonraki)
    time.sleep(5)
sayfa=1

#KaraŞahin-Milvus Migrans
url="https://xeno-canto.org/species/Milvus-migrans?pg=1"
driver.get(url)
time.sleep(5)
for i in range(8):
    html=driver.page_source
    html=BeautifulSoup(html,"html.parser")
    while trler<30:
        link = html.find("body").find("table", class_="results").find("tbody").find_all("tr")[trler].find_all("td")[11]
        link = link.find("a")
        link = link.get("href")
        driver.get(link)
        print(trler, ".indirme işlemi tamamlandı")
        trler += 1
    trler=0
    sayfa+=1
    sonraki="https://xeno-canto.org/species/Milvus-migrans?pg="+str(sayfa)
    driver.get(sonraki)
    time.sleep(5)
sayfa=1

#BayağıŞahin-Milvus Milvus
url="https://xeno-canto.org/explore?query=Milvus%20milvus"
driver.get(url)
time.sleep(5)
for i in range(6):
    html=driver.page_source
    html=BeautifulSoup(html,"html.parser")
    while trler<30:
        link = html.find("body").find("table", class_="results").find("tbody").find_all("tr")[trler].find_all("td")[11]
        link = link.find("a")
        link = link.get("href")
        driver.get(link)
        print(trler, ".indirme işlemi tamamlandı")
        trler += 1
    trler=0
    sayfa+=1
    sonraki="https://xeno-canto.org/explore?query=Milvus+milvus&pg="+str(sayfa)
    driver.get(sonraki)
    time.sleep(5)
sayfa=1

#Kartal-Haliaeetus Albicilla
url="https://xeno-canto.org/explore?query=Haliaeetus%20albicilla"
driver.get(url)
time.sleep(5)
for i in range(6):
    html=driver.page_source
    html=BeautifulSoup(html,"html.parser")
    while trler<30:
        link = html.find("body").find("table", class_="results").find("tbody").find_all("tr")[trler].find_all("td")[11]
        link = link.find("a")
        link = link.get("href")
        driver.get(link)
        print(trler, ".indirme işlemi tamamlandı")
        trler += 1
    trler=0
    sayfa+=1
    sonraki="https://xeno-canto.org/explore?query=Haliaeetus+albicilla&pg="+str(sayfa)
    driver.get(sonraki)
    time.sleep(5)
sayfa=1

#KüçükKartal-Pandion Haliaetus
url="https://xeno-canto.org/explore?query=Pandion%20haliaetus"
driver.get(url)
time.sleep(5)
for i in range(10):
    html=driver.page_source
    html=BeautifulSoup(html,"html.parser")
    while trler<30:
        link = html.find("body").find("table", class_="results").find("tbody").find_all("tr")[trler].find_all("td")[11]
        link = link.find("a")
        link = link.get("href")
        driver.get(link)
        print(trler, ".indirme işlemi tamamlandı")
        trler += 1
    trler=0
    sayfa+=1
    sonraki="https://xeno-canto.org/explore?query=Pandion+haliaetus&pg="+str(sayfa)
    driver.get(sonraki)
    time.sleep(5)
