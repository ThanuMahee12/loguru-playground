from dotenv import load_dotenv
load_dotenv()
import os

LOG_PATH = os.getenv("LOG_PATH", "logs")
ARCHIVE_PATH = os.getenv("ARCHIVE_PATH", "archive")