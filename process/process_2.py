"""
process_2.py — Structured JSON Logging

Explores:
    - serialize=True for JSON output
    - stdout JSON sink
    - File sink writing .jsonl (newline-delimited JSON)
    - Separate error JSON sink
    - Routing log dicts to correct loguru levels

Sinks:
    - stdout          : all levels, JSON
    - app.jsonl       : all levels, JSON, rotates at 20 KB
    - error.jsonl     : ERROR+ only, JSON, rotates at 20 KB

Output format (each line):
    {"text": "...", "record": {"time": ..., "level": ..., "message": ..., ...}}

Run:
    uv run python process/process_2.py
"""

import signal
import sys
from loguru import logger
from loguru_playground.generator.main import run_forever
from loguru_playground.config.env import ARCHIVE_PATH
from loguru_playground.config.logger_config import add_file_sinks

# --- Setup ---

logger.remove()

# stdout JSON sink
logger.add(sys.stdout, level="DEBUG", serialize=True)

# JSON file sinks — use serialize directly since add_file_sinks uses format
logger.add(
    str(ARCHIVE_PATH / "{time:YYYY/MM/DD}" / "process_2" / "app_{time:HHmmss}.jsonl"),
    level="DEBUG", serialize=True, rotation="20 KB", retention=5, compression="gz",
)
logger.add(
    str(ARCHIVE_PATH / "{time:YYYY/MM/DD}" / "process_2" / "error_{time:HHmmss}.jsonl"),
    level="ERROR", serialize=True, rotation="20 KB", retention=3, compression="gz",
)

# --- Log dispatcher ---

LEVEL_MAP = {
    "DEBUG": logger.debug,
    "INFO": logger.info,
    "WARNING": logger.warning,
    "ERROR": logger.error,
    "CRITICAL": logger.critical,
}

def dispatch(log: dict) -> None:
    """Route a log dict to the correct loguru level function."""
    level = log.get("level", "INFO")
    LEVEL_MAP.get(level, logger.info)(log["message"])

# --- Exit handler ---

def handle_exit(sig, frame):
    """Gracefully stop the process on SIGINT or SIGTERM."""
    logger.info("Stopping process_2.")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_exit)
signal.signal(signal.SIGTERM, handle_exit)

# --- Run ---

if __name__ == "__main__":
    logger.info("Starting process_2 — structured JSON logging")
    for log in run_forever(interval_sec=0.5):
        dispatch(log)
