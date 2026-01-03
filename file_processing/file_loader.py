from file_processing.pdf_parser import parse_pdf
from file_processing.image_ocr import extract_text_from_image
from file_processing.text_loader import load_text

def handle_file(file):
    name = file.name.lower()
    
    if name.endswith('.pdf'):
        return parse_pdf(file)
    elif name.endswith(('.png', '.jpg', '.jpeg')):
        return extract_text_from_image(file)
    if name.endswith('.txt'):
        return load_text(file)
    
    raise ValueError("Unsupported file type")