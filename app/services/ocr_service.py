import io
import platform
import pytesseract
from PIL import Image

if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


async def extract_text_from_image(file_content):
    try:
        image = Image.open(io.BytesIO(file_content.read()))
        text = pytesseract.image_to_string(image, lang='eng+rus+ara+aze+uzb+ukr+fas')
        return text.strip()
    except Exception as e:
        print(f"Error in OCR processing: {e}")
        return None
