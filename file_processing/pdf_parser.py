from pdf2image import convert_from_bytes
import numpy as np
from file_processing.ocr_engine import OCREngine

def parse_pdf(file):
    pages = convert_from_bytes(file.read())
    ocr = OCREngine.get()

    all_text = []
    for page in pages:
        img_np = np.array(page)
        res =  ocr.ocr(img_np, cls=True)
        
        for line in res[0]:
            all_text.append(line[1][0])

        return{
           "type": "pdf",
            "content": "\n".join(all_text)
        }