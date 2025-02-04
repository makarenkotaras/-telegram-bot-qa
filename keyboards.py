from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu():
    keyboard = [
        [InlineKeyboardButton("🗓 Календар засідань", callback_data="calendar")],
        [InlineKeyboardButton("📅 Запис на консультацію", callback_data="appointment")],
        [InlineKeyboardButton("❓ Поширені питання", callback_data="faq")],
        [InlineKeyboardButton("ℹ️ Інформація про суд", callback_data="court_info")],
        [InlineKeyboardButton("🔍 Контакти установ", callback_data="contacts")],
    ]
    return InlineKeyboardMarkup(keyboard)

def language_menu():
    keyboard = [
        [InlineKeyboardButton("🇺🇦 Українська", callback_data="lang_ua")],
        [InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")],
    ]
    return InlineKeyboardMarkup(keyboard)

def faq_menu(questions):
    keyboard = [[InlineKeyboardButton(q, callback_data=f"faq_{i}")] for i, q in enumerate(questions)]
    keyboard.append([InlineKeyboardButton("🔙 Назад", callback_data="main_menu")])
    return InlineKeyboardMarkup(keyboard)
