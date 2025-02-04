from telegram import InlineKeyboardMarkup

async def safe_edit_message(query, new_text, new_reply_markup: InlineKeyboardMarkup):
    try:
        if query.message and query.message.text and query.message.text != new_text:
            await query.edit_message_text(new_text, reply_markup=new_reply_markup)
    except Exception as e:
        print(f"Помилка редагування повідомлення: {e}")
