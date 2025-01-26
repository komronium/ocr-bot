import pytesseract
from PIL import Image
import io


async def extract_text_from_image(file_content):
    try:
        image = Image.open(io.BytesIO(file_content.read()))
        text = pytesseract.image_to_string(image, lang='rus+eng')
        return text.strip()
    except Exception as e:
        print(f"Error in OCR processing: {e}")
        return None
