from PIL import Image
import pytesseract

def image_extract(IMG):
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    return pytesseract.image_to_string(Image.open(f'./static/images/{IMG}'))
