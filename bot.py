from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from config import TOKEN
from handlers import (
    start, set_language, show_calendar, appointment, faq, faq_answer,
    court_info, contacts, process_appointment, main_menu_handler, help_command, text_handler
)

def main():
    app = Application.builder().token(TOKEN).build()

    # Команди
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # Обробка Callback кнопок
    app.add_handler(CallbackQueryHandler(set_language, pattern=r"^lang_"))
    app.add_handler(CallbackQueryHandler(show_calendar, pattern=r"^calendar$"))
    app.add_handler(CallbackQueryHandler(appointment, pattern=r"^appointment$"))
    app.add_handler(CallbackQueryHandler(faq, pattern=r"^faq$"))
    app.add_handler(CallbackQueryHandler(faq_answer, pattern=r"^faq_\d+$"))
    app.add_handler(CallbackQueryHandler(court_info, pattern=r"^court_info$"))
    app.add_handler(CallbackQueryHandler(contacts, pattern=r"^contacts$"))
    app.add_handler(CallbackQueryHandler(main_menu_handler, pattern=r"^main_menu$"))

    # Обробка текстових повідомлень
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_appointment))

    print("✅ Бот запущено...")
    app.run_polling()

if __name__ == "__main__":
    main()
