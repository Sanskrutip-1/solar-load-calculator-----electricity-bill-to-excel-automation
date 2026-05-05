import os
from openpyxl import load_workbook

# Get project root (go 2 levels up from backend/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Correct path to template
TEMPLATE = os.path.join(BASE_DIR, "templates", "solar_template.xlsx")

def fill_excel(data, output_path):
    wb = load_workbook(TEMPLATE)
    sheet = wb.active

    # Fill only input cells
    sheet["B2"] = data.get("units")
    sheet["B3"] = data.get("load")
    sheet["B4"] = data.get("amount")

    wb.save(output_path)