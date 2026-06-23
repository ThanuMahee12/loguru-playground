"""
process_1.py — Core Loguru Features (Plain Logs)

Explores:
    - Removing the default loguru sink
    - stdout sink with plain text format
    - File sink writing plain logs
    - Routing log dicts to correct loguru levels

Sinks:
    - stdout       : all levels, plain text
    - app.log      : all levels, plain text
    - error.log    : ERROR+ only, plain text

Run:
    uv run python loguru_playground/demo/process/process_1.py
"""

import signal
import sys
from loguru import logger
from loguru_playground.demo.generator.main import run_forever
from loguru_playground.config.logger_config import add_file_sinks

# --- Setup ---

logger.remove()

LOG_FORMAT = "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {message}"

logger.add(sys.stdout, level="DEBUG", format=LOG_FORMAT, colorize=False)
add_file_sinks("process_1", LOG_FORMAT)

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
    logger.info("Stopping process_1.")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_exit)
signal.signal(signal.SIGTERM, handle_exit)

# --- Run ---

if __name__ == "__main__":
    logger.info("Starting process_1 — core plain logs")
    for log in run_forever(interval_sec=0.5):
        dispatch(log)
