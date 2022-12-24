import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "15954332").strip()
API_HASH = os.getenv("API_HASH", "85adea6f1eaf068b707703b4846a9ced").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "5216372825:AAFRPO7v6QTsX60wrhrIfxl3T6O5wE9EWek").strip()
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "5134595693").split()))
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://navindu:navi18572@cluster0.9yrur.mongodb.net/myFirstDatabase?retryWrites=true&w=majority").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "updatechanelold")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
