# Adım 1: scrape_katalog.py dosyasında 8. satıra ilgili kategorinin 32'li gösterimi olacak şekilde ve sayfanın altındaki sekme sayısı {page_no} değişkeninde belirtilecek şekilde bir fstring olarak url kopyalanır. Buradaki amaç ilgili kategorinin her bir sekmesini ayrı ayrı inceleyip ürünlerin bilgilerini elde edebilmektir.
# Örnek 1: source = requests.get(f"https://www.dmo.gov.tr/Arama?s=&k=%7c%7cElektronik&p={page_no}&d=SM&e=3") --> 32'li Elektronik sekmesinin 1. sayfası
# Örnek 2: source = requests.get(f"https://www.dmo.gov.tr/Arama?s=&k=%7c%7cOfis%2c+K%c4%b1rtasiye%2c+Temizlik&p={page_no}&d=SM&e=3") --> 32'li Ofis Kırtasiye Temizlik sekmesinin 1. sayfası
# Örnek 3: source = requests.get(f"https://www.dmo.gov.tr/Arama?s=&k=%7c%7c%c4%b0%c5%9f+Makineleri&p={page_no}&d=SM&e=3") --> 32'li İş Makineleri sekmesinin 1. sayfası

# Adım 2: scrape_katalog.py dosyasında 39. satırdaki requests.get() metodunun parametresine ilgili kategorinin url'si kopyalanır. Buradaki amaç ilgili kategoride bulunan toplam ürün sayısını tespit etmektir.
# Örnek 1: source = requests.get("https://www.dmo.gov.tr/Arama?k=%7c%7cElektronik")
# Örnek 2: source = requests.get("https://www.dmo.gov.tr/Arama?k=%7c%7cOfis%2c+K%c4%b1rtasiye%2c+Temizlik")
# Örnek 3: source = requests.get("https://www.dmo.gov.tr/Arama?k=%7c%7c%c4%b0%c5%9f+Makineleri")
