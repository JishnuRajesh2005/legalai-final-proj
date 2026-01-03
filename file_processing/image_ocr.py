from PIL import Image
import numpy as np
from  file_processing.ocr_engine import OCREngine

def extract_text_from_image(image_file):
    image = Image.open(image_file).convert("RGB")
    img_np = np.array(image)

    ocr = OCREngine.get()
    result = ocr.ocr(img_np, cls=True)

    text_lines = []
    for line in result[0]:
        text_lines.append(line[1][0])

    return{
        "type": "image",
        "content": "\n".join(text_lines)
    }
    