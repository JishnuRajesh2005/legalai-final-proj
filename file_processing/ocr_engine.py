from paddleocr import PaddleOCR

class OCREngine:
    _instance = None

    @staticmethod
    def get():
        if OCREngine._instance is None:
            OCREngine._instance = PaddleOCR(use_angle_cls=True, lang='en')
        return OCREngine._instance