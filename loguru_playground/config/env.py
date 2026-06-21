import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

LOG_PATH = Path(os.getenv("LOG_PATH", "logs"))
ARCHIVE_PATH = Path(os.getenv("ARCHIVE_PATH", "archive"))