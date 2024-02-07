import fitz   # access by pip install PyMuPDF

def extract_text_from_pdf(input_path, start_page=0, end_page=None):
    doc = fitz.open(input_path)
    text_by_page = []

    for page_num in range(start_page, end_page):
        page = doc[page_num]
        page_txt = page.get_text()
        text_by_page.append(page_txt)

    extracted_text = ''.join(text_by_page)
    doc.close()
    return extracted_text

def save_txt(text, output_path):
    with open(output_path, 'w', encoding='unicode') as output_file:
        output_file.write(text)
    output_file.close()


