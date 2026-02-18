import fitz  # PyMuPDF


def extract_text_from_bytes(file_bytes: bytes):
    # Open document from bytes
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    
    print("Number of pages:", len(doc))
    
    # Extract text from all pages
    text = ""
    for page in doc:
        text += page.get_text()
    
    return text


if __name__ == "__main__":
    with open("chat_bot_app/data_loader/stock_market_parameters_formulas 1.pdf", "rb") as f:
        file_bytes = f.read()
    
    extracted_text = extract_text_from_bytes(file_bytes)
    print(extracted_text)
