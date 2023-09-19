from bs4 import BeautifulSoup
import requests

with open("ornek_katalog.html", "r") as file:
    soup = BeautifulSoup(file, "html.parser")

# Find all the <div> elements with class "product-item"
product_items = set(soup.find_all('div', class_='product-item'))

# Initialize a list to store the extracted href values
href_values = []

# Loop through each product item and extract the href value
for product_item in product_items:
    # Find the <a> element within the product item
    a_element = product_item.find('a', href=True)  # Check for the presence of href attribute
    if a_element:
        href_value = a_element['href']  # Extract the href attribute value
        href_values.append(href_value)  # Append to the list

href_values = set(href_values)

# Print the extracted href values
for href_value in href_values:
    print(href_value)
    
# Call scrape.py for every href_value

# Create elektronik.py, ofis_kirtasiye.py etc. 