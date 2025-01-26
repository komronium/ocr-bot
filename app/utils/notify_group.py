from aiogram import Bot
from config import settings

async def notify_group_about_new_user(bot: Bot, user):
    try:
        message = (
            f"*👤 New Member!\n*"
            f"*🆔 ID:* {user.id}\n"
            f"*📛 Username:* {user.first_name} {user.last_name if user.last_name else ''}"
            f"*✏️ Name:* @{user.username if user.username else 'N/A'}\n"
        )
        await bot.send_message(settings.GROUP_ID, message)
    except Exception as e:
        print(f"Error notifying group: {e}")
