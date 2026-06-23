"""
process_3.py — Exception Handling with Loguru

Explores:
    - logger.catch() as decorator and context manager
    - logger.exception() for logging with full traceback
    - diagnose=True for variable inspection in tracebacks
    - Catching exceptions from generator errors
    - Graceful error recovery in infinite loops

Sinks:
    - stdout          : all levels, plain text, diagnose=True
    - app.log         : all levels, rotates at 20 KB
    - error.log       : ERROR+ only, with full tracebacks

Run:
    uv run python process/process_3.py
"""

import signal
import sys
import random
from loguru import logger
from loguru_playground.generator.main import run_forever
from loguru_playground.config.logger_config import add_file_sinks

# --- Setup ---

logger.remove()

LOG_FORMAT = "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {message}"

logger.add(sys.stdout, level="DEBUG", format=LOG_FORMAT, colorize=False, diagnose=True, backtrace=True)
add_file_sinks("process_3", LOG_FORMAT, diagnose=True, backtrace=True)

# --- Simulated risky operations ---

def risky_parse(message: str) -> str:
    """Randomly raises exceptions to simulate real pipeline failures."""
    roll = random.random()
    if roll < 0.05:
        raise ValueError(f"Invalid format in message: {message[:30]}")
    if roll < 0.08:
        raise KeyError("missing_field")
    if roll < 0.10:
        raise ConnectionError("Upstream service unavailable")
    return message

# --- Exception handling patterns ---

@logger.catch
def process_with_decorator(log: dict) -> None:
    """Pattern 1: logger.catch as decorator — catches and logs exceptions automatically."""
    message = risky_parse(log["message"])
    logger.log(log["level"], message)


def process_with_context_manager(log: dict) -> None:
    """Pattern 2: logger.catch as context manager — catches within a block."""
    with logger.catch():
        message = risky_parse(log["message"])
        logger.log(log["level"], message)


def process_with_exception(log: dict) -> None:
    """Pattern 3: logger.exception — manual try/except with full traceback."""
    try:
        message = risky_parse(log["message"])
        logger.log(log["level"], message)
    except Exception as e:
        logger.exception(f"Failed to process log: {e}")


# Rotate through all three patterns
HANDLERS = [
    process_with_decorator,
    process_with_context_manager,
    process_with_exception,
]

# --- Exit handler ---

def handle_exit(sig, frame):
    """Gracefully stop the process on SIGINT or SIGTERM."""
    logger.info("Stopping process_3.")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_exit)
signal.signal(signal.SIGTERM, handle_exit)

# --- Run ---

if __name__ == "__main__":
    logger.info("Starting process_3 — exception handling patterns")
    for i, log in enumerate(run_forever(interval_sec=0.5)):
        HANDLERS[i % len(HANDLERS)](log)
