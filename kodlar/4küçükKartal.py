from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
import os


#KüçükKartal

url="https://search.macaulaylibrary.org/catalog?taxonCode=osprey&mediaType=audio"
driver=webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(450)

dosyaSayisi=1
satir=0
sutun=0
sayfaKaynak=driver.page_source
sayfaKaynak=BeautifulSoup(sayfaKaynak,"html.parser")
divs=sayfaKaynak.find("div",class_="ResultsGallery").find_all("div",class_="ResultsGallery-row")

for i in range(len(divs)-1):
    sutun = 0
    link=sayfaKaynak.find("div",class_="ResultsGallery")
    link=link.find_all("div",class_="ResultsGallery-row")[satir]
    for i in range(3):
        link1=link.find_all("a")[sutun]
        link1=link1.get("href")
        sutun+=1
        driver.execute_script("window.open(arguments[0],'_blank');", link1)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(2)
        link2=driver.page_source
        link2=BeautifulSoup(link2,"html.parser")
        link2=link2.find("div", class_="SpectrogramPlayer-frame").find("audio")
        indirilecekLink=link2.get("src")
        driver.close()
        response = requests.get(indirilecekLink)
        driver.switch_to.window(driver.window_handles[0])
        masaustu_klasoru = os.path.join(os.path.expanduser("~"), "Desktop", "yazLab", "kuşSesleri", "küçükKartal")
        dosya_yolu = os.path.join(masaustu_klasoru, str(dosyaSayisi) + ".KüçükKartal.mp3")
        dosyaSayisi += 1
        response = requests.get(indirilecekLink)
        with open(dosya_yolu, "wb") as file:
            file.write(response.content)
    satir+=1
driver.quit()
time.sleep(5)