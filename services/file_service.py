import os

from services.pdf_service import read_pdf
from services.csv_service import read_csv
from services.excel_service import read_excel


def extract_text(uploaded_file):

    extension = os.path.splitext(uploaded_file.name)[1].lower()

    if extension == ".pdf":
        return read_pdf(uploaded_file)

    elif extension == ".txt":
        return uploaded_file.read().decode("utf-8")

    elif extension == ".csv":
        return read_csv(uploaded_file)

    elif extension in [".xlsx", ".xls"]:
        return read_excel(uploaded_file)

    raise ValueError("Unsupported file format")
