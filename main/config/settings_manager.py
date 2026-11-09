# settings_manager.py

from dotenv import load_dotenv
import json
import os


def _env(name, default=None):
    """مقدار متغیر محیطی را برمی‌گرداند و رشته‌های خالی را نادیده می‌گیرد."""
    value = os.getenv(name)
    if value is None:
        return default
    value = value.strip()
    return value if value else default


class Settings:
    def __init__(self):
        load_dotenv()

        # پیش‌فرض محیط توسعه: SQLite تا پروژه بدون نصب سرور دیتابیس اجرا شود.
        # برای MySQL/PostgreSQL کافی است DB_ENGINE را در .env تنظیم کنید.
        self.db_engine = _env('DB_ENGINE', 'django.db.backends.sqlite3')
        self.db_name = _env('DB_NAME', 'db.sqlite3')
        self.db_user = _env('DB_USER')
        self.db_password = _env('DB_PASSWORD')
        self.db_host = _env('DB_HOST')

        raw_port = _env('DB_PORT')
        try:
            self.db_port = int(raw_port) if raw_port else None
        except ValueError:
            raise ValueError(f'DB_PORT باید یک عدد باشد، مقدار فعلی: {raw_port!r}')

        self.zarinpal_merchant_id = _env('ZARINPAL_MERCHANT_ID')
        self.zarinpal_sandbox = (_env('ZARINPAL_SANDBOX', 'True').lower() == 'true')

        self.secret_key = _env('SECRET_KEY')

        raw_hosts = _env('ALLOWED_HOSTS', '["*"]')
        try:
            hosts = json.loads(raw_hosts)
        except ValueError:
            # پشتیبانی از حالت قدیمی: ALLOWED_HOSTS=localhost,127.0.0.1
            hosts = [h.strip() for h in raw_hosts.split(',') if h.strip()]
        self.allowed_hosts = hosts if isinstance(hosts, list) else [str(hosts)]


settings_instance = Settings()
