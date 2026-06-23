"""
process_4.py — Binding and Context with Loguru

Explores:
    - logger.bind() — attach static context fields to a logger instance
    - logger.contextualize() — attach temporary context for a block
    - Combining bind and contextualize for structured context propagation
    - Per-log-type context enrichment (pipeline, user, service)

Sinks:
    - stdout          : all levels, plain text with context fields
    - app.log         : all levels, rotates at 20 KB
    - error.log       : ERROR+ only, rotates at 20 KB

Run:
    uv run python process/process_4.py
"""

import signal
import sys
import random
from loguru import logger
from loguru_playground.generator.main import run_forever, LOG_BUILDERS
from loguru_playground.config.logger_config import add_file_sinks

# --- Setup ---

logger.remove()

LOG_FORMAT = "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {extra[service]} | {extra[env]} | {message}"

logger.add(sys.stdout, level="DEBUG", format=LOG_FORMAT, colorize=False)
add_file_sinks("process_4", LOG_FORMAT)

# --- Bound loggers — static context per service ---

pipeline_logger = logger.bind(service="pipeline", env="production")
auth_logger = logger.bind(service="auth", env="production")
dq_logger = logger.bind(service="data-quality", env="staging")
system_logger = logger.bind(service="system", env="production")
default_logger = logger.bind(service="app", env="production")

# --- Level dispatcher ---

LEVEL_MAP = {
    "DEBUG": "debug",
    "INFO": "info",
    "WARNING": "warning",
    "ERROR": "error",
    "CRITICAL": "critical",
}

def dispatch(bound_logger, log: dict) -> None:
    """Route a log dict to the correct level on a bound logger."""
    level = log.get("level", "INFO")
    getattr(bound_logger, LEVEL_MAP.get(level, "info"))(log["message"])


def dispatch_with_context(log: dict) -> None:
    """Pattern: logger.contextualize() — temporary context for a request/job scope."""
    job_id = f"job-{random.randint(1000, 9999)}"
    user = f"user-{random.randint(1, 100)}"
    with logger.contextualize(job_id=job_id, user=user):
        level = log.get("level", "INFO")
        getattr(logger, LEVEL_MAP.get(level, "info"))(log["message"])


# --- Log type router ---

def route(log: dict) -> None:
    """Route log to appropriate bound logger based on message prefix."""
    msg = log.get("message", "")
    if msg.startswith("PIPELINE"):
        dispatch(pipeline_logger, log)
    elif msg.startswith("AUTH"):
        dispatch(auth_logger, log)
    elif msg.startswith("DQ"):
        dispatch(dq_logger, log)
    elif msg.startswith("SYSTEM"):
        dispatch(system_logger, log)
    else:
        dispatch(default_logger, log)


# --- Exit handler ---

def handle_exit(sig, frame):
    """Gracefully stop the process on SIGINT or SIGTERM."""
    logger.bind(service="app", env="production").info("Stopping process_4.")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_exit)
signal.signal(signal.SIGTERM, handle_exit)

# --- Run ---

if __name__ == "__main__":
    default_logger.info("Starting process_4 — binding and context")
    for log in run_forever(interval_sec=0.5):
        route(log)
