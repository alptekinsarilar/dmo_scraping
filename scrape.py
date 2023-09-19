from bs4 import BeautifulSoup
import requests

try:
    #source = requests.get("https://www.dmo.gov.tr/Katalog/Urun/Detay/1171329_1059351")
    #source.raise_for_status()
    #soup = BeautifulSoup(source.text, "html.parser")
    
    with open("ornek_urun.html", "r") as file:
        soup = BeautifulSoup(file, "html.parser")
    
    """ Part 1 """
    
    baslik = soup.find("div", class_="title").text
    tedarikci = soup.find("a", class_="available").text.strip()
    aciklama = soup.find_all("p")[0].string
    vergisiz_fiyat = soup.find("div", class_="price-current").text
    vergili_fiyat = soup.find("div", class_="price-prev").text
    
    birim_fiyat = soup.find("div", class_="excerpt").find_all("div")[8].text.strip()
    kdv = soup.find("div", class_="excerpt").find_all("div")[9].text.strip()
    dmo_urun_kodu = soup.find("div", class_="excerpt").find_all("div")[10].text.strip()
    olcu_birimi = soup.find("div", class_="excerpt").find_all("div")[11].text.strip()
    orijinal_urun_kodu = soup.find("div", class_="excerpt").find_all("div")[12].text.strip()
    garanti_suresi = soup.find("div", class_="excerpt").find_all("div")[13].text.strip()
    yerli_katki_orani = soup.find("div", class_="excerpt").find_all("div")[14].text.strip()
    teknolojik_duzey = soup.find("div", class_="excerpt").find_all("div")[15].text.strip()
    yerli_mali_belgesi_gecerlilik_tarihi = soup.find("div", class_="excerpt").find_all("div")[16].text.strip()
    
    #print(baslik)
    #print(tedarikci)
    #print()
    #print(aciklama)
    #print(vergisiz_fiyat)
    #print(vergili_fiyat)
    
    #print(birim_fiyat)
    #print(kdv)
    #print(dmo_urun_kodu)
    #print(olcu_birimi)
    #print(orijinal_urun_kodu)
    #print(garanti_suresi)
    #print(yerli_katki_orani)
    #print(teknolojik_duzey)
    #print(yerli_mali_belgesi_gecerlilik_tarihi)
    
    """ Part 2 """
    
    satis_kosullari = soup.find("section", class_="fadeInUp").text.strip()
    
    #print(satis_kosullari)
    
    """ Part 3 """
    
    urun_ozellikleri = soup.find_all("section", class_="fadeInUp")[1].text.strip()
    
    print(urun_ozellikleri)
    
except Exception as e:
    print(e)