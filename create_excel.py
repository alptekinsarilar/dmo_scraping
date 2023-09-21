import os
from openpyxl import Workbook

# Set file path
filepath = "./dmo_urunler.xlsx"

# Check if the file already exists
if not os.path.exists(filepath):
    wb = Workbook()
    wb.save(filepath)
    print(f"New workbook created at {filepath}")
else:
    print(f"File {filepath} already exists. Skipping workbook creation.")
