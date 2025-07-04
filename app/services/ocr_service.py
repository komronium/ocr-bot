import io
import numpy as np
import cv2
import platform
import pytesseract
from PIL import Image

if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


async def extract_text_from_image(file_content):
    try:
        pil_image = Image.open(io.BytesIO(file_content.read()))
        image = np.array(pil_image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        thresh = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY, 11, 2
        )

        text = pytesseract.image_to_string(thresh, lang='eng+rus+ara+aze+uzb+ukr+fas')
        return text.strip()
    except Exception as e:
        print(f"Error in OCR processing: {e}")
        return None
