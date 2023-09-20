from bs4 import BeautifulSoup
import requests
import math
from scrape import scrape_product

def scrape_catalog_with_page_number(page_no):
    try:
        source = requests.get(f"https://www.dmo.gov.tr/Arama?s=&k=%7c%7c%c4%b0%c5%9f+Makineleri&p={page_no}&d=SM&e=3")
        source.raise_for_status()
        soup = BeautifulSoup(source.text, "html.parser")

        # Find all the <div> elements with class "product-item"
        product_items = soup.find_all('div', class_='product-item')

        # Initialize a list to store the extracted href values
        href_values = []

        # Loop through each product item and extract the href value
        for product_item in product_items:
            # Find the <a> element within the product item
            a_element = product_item.find('a', href=True)  # Check for the presence of href attribute
            if a_element:
                href_value = a_element['href']  # Extract the href attribute value
                href_values.append(href_value)  # Append to the list

        # Somehow for 32 product there were 64 href so we need to make them unique
        # Probably there are 2 href for a product, 1 for image 1 for text
        href_values = set(href_values)

        # Print the extracted href values
        for href_value in href_values:
            scrape_product(href_value)
            
    except Exception as e:
        print(e)     
    
            
def get_total_product_number():
    try:
        source = requests.get("https://www.dmo.gov.tr/Arama?k=%7c%7c%c4%b0%c5%9f+Makineleri")
        source.raise_for_status()
        soup = BeautifulSoup(source.text, "html.parser")

        # Find all the <div> elements with class "product-item"
        result_counter = soup.find('div', class_='result-counter')
        
        number = result_counter.find('span').text
        
        return int(number)
    except Exception as e:
            print(e)

total_page_no = math.ceil(get_total_product_number() / 32)

# Now we need to scrape every page from "1" to "math.ceil(get_total_product_number() / 32)"


for page_no in range(1, total_page_no+1):
    print("page no in catalog:", page_no)
    scrape_catalog_with_page_number(page_no)

