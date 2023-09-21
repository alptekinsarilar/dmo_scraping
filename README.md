## Adım 1: scrape_katalog.py dosyasında 8. satıra ilgili kategorinin 32'li gösterimi olacak şekilde ve sayfanın altındaki sekme sayısı {page_no} değişkeninde belirtilecek şekilde bir fstring olarak url kopyalanır. Buradaki amaç ilgili kategorinin her bir sekmesini ayrı ayrı inceleyip ürünlerin bilgilerini elde edebilmektir.
* Örnek 1: source = requests.get(f"https://www.dmo.gov.tr/Arama?s=&k=%7c%7cElektronik&p={page_no}&d=SM&e=3") --> 32'li Elektronik sekmesinin 1. sayfası
* Örnek 2: source = requests.get(f"https://www.dmo.gov.tr/Arama?s=&k=%7c%7cOfis%2c+K%c4%b1rtasiye%2c+Temizlik&p={page_no}&d=SM&e=3") --> 32'li Ofis Kırtasiye Temizlik sekmesinin 1. sayfası
* Örnek 3: source = requests.get(f"https://www.dmo.gov.tr/Arama?s=&k=%7c%7cMobilya%2c+Tekstil&p={page_no}&d=SM&e=3") --> 32'li Mobilya Tekstil sekmesinin 1. sayfası
* Örnek 4: source = requests.get(f"https://www.dmo.gov.tr/Arama?s=&k=%7c%7cTa%c5%9f%c4%b1t%2c+Ak%c3%bc%2c+Lastik&p={page_no}&d=SM&e=3") --> 32'li Taşıt Akü Lastik sekmesinin 1. sayfası
* Örnek 5: source = requests.get(f"https://www.dmo.gov.tr/Arama?s=&k=%7c%7c%c4%b0%c5%9f+Makineleri&p={page_no}&d=SM&e=3") --> 32'li İş Makineleri sekmesinin 1. sayfası
Örnek 6: source = requests.get(f"https://www.dmo.gov.tr/Arama?s=&k=%7c%7cSa%c4%9fl%c4%b1k%2c+Medikal+%c3%9cr%c3%bcnler&p={page_no}&d=SM&e=3") --> 32'li Sağlık Medikal Ürünler sekmesinin 1. sayfası
* Örnek 7: source = requests.get(f"https://www.dmo.gov.tr/Arama?s=&k=%7c%7cEkipmanlar&p={page_no}&d=SM&e=3") --> 32'li Ekipmanlar sekmesinin 1. sayfası

## Adım 2: scrape_katalog.py dosyasında 39. satırdaki requests.get() metodunun parametresine ilgili kategorinin url'si kopyalanır. Buradaki amaç ilgili kategoride bulunan toplam ürün sayısını tespit etmektir.
* Örnek 1: source = requests.get("https://www.dmo.gov.tr/Arama?k=%7c%7cElektronik")
* Örnek 2: source = requests.get("https://www.dmo.gov.tr/Arama?k=%7c%7cOfis%2c+K%c4%b1rtasiye%2c+Temizlik")
* Örnek 3: source = requests.get("https://www.dmo.gov.tr/Arama?k=%7c%7cMobilya%2c+Tekstil")
* Örnek 4: source = requests.get("https://www.dmo.gov.tr/Arama?k=%7c%7cTa%c5%9f%c4%b1t%2c+Ak%c3%bc%2c+Lastik")
* Örnek 5: source = requests.get("https://www.dmo.gov.tr/Arama?k=%7c%7c%c4%b0%c5%9f+Makineleri")
* Örnek 6: source = requests.get("https://www.dmo.gov.tr/Arama?k=%7c%7cSa%c4%9fl%c4%b1k%2c+Medikal+%c3%9cr%c3%bcnler")
* Örnek 7: source = requests.get("https://www.dmo.gov.tr/Arama?k=%7c%7cEkipmanlar")

## Programın doğru şekilde çalıştırılabilmesi için dosyalarla aynı dizinde bulunan "dmo_urunler.xlsx" dosyası önceden oluşturulmuş olmalıdır. Sadece excelin oluşturulması yeterlidir. Sheet'lerin önceden oluşturulmasına gerek yoktur. create_excel.py dosyası bu işlemi gerçekleştirmeye yardımcı olur.

## Arzu edilen kategorideki ürünlerin aratılması için belirtilen yerlere örneklerde'ki url'ler yapıştırılmalıdır ve ardından scrape_katalog.py dosyası çalıştırılmalıdır.