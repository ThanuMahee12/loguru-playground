import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

LOG_PATH = Path(os.getenv("LOG_PATH", "logs"))
ARCHIVE_PATH = Path(os.getenv("ARCHIVE_PATH", "archive"))
DB_PATH=Path(os.getenv("DB_PATH","db"))