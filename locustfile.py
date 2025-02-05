
from locust import HttpUser, TaskSet, task, between
import random
import config  # Імпортуємо файл з конфігурацією

CHAT_ID = "677103390"

class UserBehavior(TaskSet):
    @task(1)
    def send_start_command(self):
        """Користувач надсилає команду /start"""
        self.client.get(f"https://api.telegram.org/bot{config.TOKEN}/sendMessage",
                        params={"chat_id": CHAT_ID, "text": "/start"})

    @task(1)
    def select_language(self):
        """Користувач вибирає мову (наприклад, українську)"""
        self.client.get(f"https://api.telegram.org/bot{config.TOKEN}/callback_query",
                        params={"chat_id": CHAT_ID, "data": "lang_ua"})

    @task(1)
    def show_calendar(self):
        """Користувач переглядає календар"""
        self.client.get(f"https://api.telegram.org/bot{config.TOKEN}/callback_query",
                        params={"chat_id": CHAT_ID, "data": "show_calendar"})

    @task(1)
    def book_appointment(self):
        """Користувач записується на прийом"""
        random_time = random.choice(["10:00", "12:30", "15:00"])
        self.client.get(f"https://api.telegram.org/bot{config.TOKEN}/sendMessage",
                        params={"chat_id": CHAT_ID, "text": f"Запис на {random_time}"})

class TelegramBotUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 3)  # Затримка між запитами 1-3 секунди
