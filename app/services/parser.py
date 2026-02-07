import pdfplumber

def extract_text(file):
    file.file.seek(0)

    if file.filename.lower().endswith(".pdf"):
        with pdfplumber.open(file.file) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)

    return file.file.read().decode("utf-8", errors="ignore")

