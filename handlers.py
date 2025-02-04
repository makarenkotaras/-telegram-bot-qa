from telegram import Update
from telegram.ext import ContextTypes
import json
from keyboards import main_menu, language_menu, faq_menu
from utils import safe_edit_message

# Завантаження запитань та відповідей
with open("data.json", "r", encoding="utf-8") as file:
    FAQ_DATA = json.load(file)

# Завантаження тестових даних для календаря
SCHEDULE = [
    "🗓 5 лютого - Справа №12345: 10:00, Суддя Іваненко",
    "🗓 7 лютого - Справа №67890: 14:30, Суддя Петренко",
    "🗓 12 лютого - Справа №54321: 09:00, Суддя Коваленко",
]

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Виберіть мову:", reply_markup=language_menu())

# Вибір мови
async def set_language(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    context.user_data["language"] = query.data.split("_")[1]
    await safe_edit_message(query, "Оберіть дію:", main_menu())

# Календар судових засідань
async def show_calendar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    schedule_text = "\n".join(SCHEDULE)
    await safe_edit_message(query, f"📅 Розклад засідань:\n{schedule_text}", main_menu())

# Онлайн-запис
async def appointment(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await safe_edit_message(query, "📌 Введіть ваше ім'я та бажаний час запису:", None)

# Обробка запису на консультацію
async def process_appointment(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_text = update.message.text
    await update.message.reply_text(f"✅ Ваш запис підтверджено: {user_text}")

# Поширені питання
async def faq(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await safe_edit_message(query, "Оберіть питання:", faq_menu(list(FAQ_DATA.keys())))

# Відповідь на питання
async def faq_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    question_index = int(query.data.split("_")[1])
    question = list(FAQ_DATA.keys())[question_index]
    answer = FAQ_DATA[question]
    await safe_edit_message(query, f"❓ {question}\n\n💬 {answer}", faq_menu(list(FAQ_DATA.keys())))

# Інформація про суд
async def court_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await safe_edit_message(query, "ℹ️ Суд розташований за адресою: вул. Центральна, 15, Київ.", main_menu())

# Контакти інших установ
async def contacts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await safe_edit_message(query, "📞 Нотаріуси: +380 44 123 45 67\n📞 Міграційна служба: +380 44 987 65 43", main_menu())

# Головне меню
async def main_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await safe_edit_message(query, "Оберіть дію:", main_menu())

# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("ℹ️ Використовуйте /start для початку роботи.")

# Обробка тексту
async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Не зрозуміло, скористайтеся кнопками меню.")
