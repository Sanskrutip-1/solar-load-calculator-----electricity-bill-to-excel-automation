from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import os

from ocr import extract_text
from extractor import extract_bill_data
from excel_writer import fill_excel

app = FastAPI()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.post("/process/")
async def process_bill(file: UploadFile = File(...)):
    
    file_path = f"{UPLOAD_DIR}/{file.filename}"
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Step 1: OCR
    text = extract_text(file_path)

    # Step 2: Extract Data
    data = extract_bill_data(text)

    # Step 3: Fill Excel
    output_file = f"{OUTPUT_DIR}/output_{file.filename}.xlsx"
    fill_excel(data, output_file)

    return FileResponse(output_file, filename="solar_output.xlsx")