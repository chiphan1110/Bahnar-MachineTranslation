from extract_txt import *
from clean_text import *

def clean(input_path, output_path):
    raw, processed, bahnar_path, vn_path = output_path
    text = extract_text_from_pdf(input_path, 34, 468)
    save_txt(text, raw)

    text = remove_header_footer(text)
    text = remove_empty(text)
    text = sentence_concat(text)
    save_txt(text, processed)

    bahnar, vietnamese = separate_language(text)
    save_txt(bahnar, bahnar_path)
    save_txt(vietnamese, vn_path)


if __name__ == '__main__':
    pdf_path = 'raw-data/law-text.pdf'
    raw = 'raw-data/raw.txt'
    processed = 'processed-data/processed.txt'
    bahnar = 'processed-data/bahnar.txt'
    vietnamese = 'processed-data/vietnamese.txt'

    clean(pdf_path, (raw, processed, bahnar, vietnamese))


