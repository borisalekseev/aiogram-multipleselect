from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())


BOT_TOKEN = os.getenv("TOKEN")
