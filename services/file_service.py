"""
File extraction service.
"""

import os


def extract_text(uploaded_file):
    """
    Extract text from uploaded files.

    Supported:
    - PDF
    - TXT
    - CSV
    - Excel
    """

    extension = os.path.splitext(uploaded_file.name)[1].lower()

    if extension == ".txt":
        return uploaded_file.read().decode("utf-8", errors="ignore")

    if extension == ".pdf":
        from services.pdf_service import read_pdf
        return read_pdf(uploaded_file)

    if extension == ".csv":
        from services.csv_service import read_csv
        return read_csv(uploaded_file)

    if extension in (".xlsx", ".xls"):
        from services.excel_service import read_excel
        return read_excel(uploaded_file)

    raise ValueError(f"Unsupported file type: {extension}")