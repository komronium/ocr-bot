from aiogram import types, Router, F
from app.services.ocr_service import extract_text_from_image
from app.services.user_service import UserService

router = Router()


@router.message(F.photo)
async def handle_image(message: types.Message):
    try:
        processing_msg = await message.reply("Processing your image...")

        photo = message.photo[-1]
        file = await message.bot.get_file(photo.file_id)
        file_path = file.file_path

        downloaded_file = await message.bot.download_file(file_path)
        text = await extract_text_from_image(downloaded_file)

        if text:
            await UserService().add_conversion(message.from_user.id)
            await processing_msg.edit_text(f"*Extracted text:*\n\n{text}", parse_mode='Markdown')
        else:
            await processing_msg.edit_text("No text was found in the image.")

    except Exception as e:
        await message.reply("Sorry, an error occurred while processing your image.")
