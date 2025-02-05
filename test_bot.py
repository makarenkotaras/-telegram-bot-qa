import pytest
import asyncio
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from handlers import start, set_language, show_calendar, process_appointment, faq_answer
from unittest.mock import AsyncMock, MagicMock, ANY  # Додано імпорт ANY


@pytest.mark.asyncio
async def test_start_command():
    update = MagicMock()
    update.message = MagicMock()
    update.message.text = "/start"
    update.message.reply_text = AsyncMock()

    await start(update, None)

    update.message.reply_text.assert_called_once_with(
        "Виберіть мову:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🇺🇦 Українська", callback_data="lang_ua")],
            [InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")]
        ])
    )


@pytest.mark.asyncio
async def test_set_language():
    query = MagicMock()
    query.data = "lang_ua"
    query.answer = AsyncMock()
    query.edit_message_text = AsyncMock()

    context = MagicMock()
    context.user_data = {}

    query.callback_query = query  # Додаємо для сумісності з update.callback_query

    await set_language(query, context)

    assert context.user_data["language"] == "ua"
    query.edit_message_text.assert_called_once_with(
        "Оберіть дію:",
        reply_markup=ANY  # Дозволяє будь-яке значення для reply_markup
    )


@pytest.mark.asyncio
async def test_show_calendar():
    query = MagicMock()
    query.answer = AsyncMock()
    query.edit_message_text = AsyncMock()

    query.callback_query = query  # Аналогічно

    await show_calendar(query, None)

    query.answer.assert_called_once()
    query.edit_message_text.assert_called_once()


@pytest.mark.asyncio
async def test_process_appointment():
    update = MagicMock()
    update.message = MagicMock()
    update.message.text = "Запис на 10:00"
    update.message.reply_text = AsyncMock()

    await process_appointment(update, None)

    update.message.reply_text.assert_called_once_with("✅ Ваш запис підтверджено: Запис на 10:00")


@pytest.mark.asyncio
async def test_faq_answer():
    query = MagicMock()
    query.data = "faq_0"
    query.answer = AsyncMock()
    query.edit_message_text = AsyncMock()

    query.callback_query = query  # Додаємо для коректної роботи

    await faq_answer(query, None)

    query.answer.assert_called_once()
    query.edit_message_text.assert_called_once()
