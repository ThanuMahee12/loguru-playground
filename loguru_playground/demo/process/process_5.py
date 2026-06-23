"""
process_5.py — Async Logging with Loguru

Explores:
    - enqueue=True — non-blocking thread-safe logging via internal queue
    - asyncio-based log generation
    - logger.complete() — flush all queued log messages before exit
    - Concurrent log producers simulating parallel pipeline workers

Sinks:
    - stdout          : all levels, enqueued
    - app.log         : all levels, enqueued, rotates at 20 KB
    - error.log       : ERROR+ only, enqueued, rotates at 20 KB

Run:
    uv run python loguru_playground/demo/process/process_5.py
"""

import signal
import sys
import asyncio
import random
from loguru import logger
from loguru_playground.demo.generator.main import LOG_BUILDERS
from loguru_playground.config.logger_config import add_file_sinks

# --- Setup ---

logger.remove()

LOG_FORMAT = "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {extra[worker]} | {message}"

logger.add(
    sys.stdout,
    level="DEBUG",
    format=LOG_FORMAT,
    colorize=False,
    enqueue=True,
)
add_file_sinks("process_5", LOG_FORMAT)

# --- Async worker ---

LEVEL_MAP = {
    "DEBUG": logger.debug,
    "INFO": logger.info,
    "WARNING": logger.warning,
    "ERROR": logger.error,
    "CRITICAL": logger.critical,
}

async def worker(worker_id: str, interval: float, count: int) -> None:
    """Simulate a pipeline worker emitting logs concurrently."""
    bound = logger.bind(worker=worker_id)
    for _ in range(count):
        log = random.choice(LOG_BUILDERS)()
        level = log.get("level", "INFO")
        getattr(bound, level.lower())(log["message"])
        await asyncio.sleep(interval)

async def run_async(num_workers: int = 4, logs_per_worker: int = 50) -> None:
    """Run multiple async workers concurrently."""
    workers = [
        worker(f"worker-{i+1}", interval=random.uniform(0.1, 0.5), count=logs_per_worker)
        for i in range(num_workers)
    ]
    await asyncio.gather(*workers)
    await logger.complete()

# --- Exit handler ---

def handle_exit(sig, frame):
    """Gracefully stop the process on SIGINT or SIGTERM."""
    logger.bind(worker="main").info("Stopping process_5.")
    asyncio.get_event_loop().run_until_complete(logger.complete())
    sys.exit(0)

signal.signal(signal.SIGINT, handle_exit)
signal.signal(signal.SIGTERM, handle_exit)

# --- Run ---

if __name__ == "__main__":
    logger.bind(worker="main").info("Starting process_5 — async logging with enqueue=True")
    asyncio.run(run_async(num_workers=4, logs_per_worker=50))
    logger.bind(worker="main").info("process_5 complete.")
