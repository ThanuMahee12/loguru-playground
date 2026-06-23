# loguru-playground

A hands-on exploration of loguru's logging capabilities for data pipelines and ML workflows.

## Overview

This repo explores loguru features through isolated process scripts, each covering a specific logging pattern. Random log data is generated using `faker` to simulate realistic data science and ML workloads including HTTP requests, database queries, authentication events, data quality checks, pipeline runs, system metrics, errors, warnings, and alerts.

## Project Structure

```
loguru_playground/
    config/
        env.py              # LOG_PATH, ARCHIVE_PATH as Path objects from .env
        logger.yaml         # per-process sink configuration
        logger_config.py    # setup_logger() and add_file_sinks() helpers
    generator/
        main.py             # faker-based log generators + run_forever()
process/
    process_1.py            # core plain text logging + size-based rotation
    process_2.py            # structured JSON logging (.jsonl)
    process_3.py            # exception handling + tracebacks
    process_4.py            # binding and context (logger.bind, contextualize)
    process_5.py            # async logging (enqueue=True, concurrent workers)
```

## Processes

### process_1 — Core Plain Logs + Size-Based Rotation
- `logger.remove()` — clean slate, no default sink
- stdout plain text sink
- File sinks with `rotation="20 KB"`, `retention=5`, `compression="gz"`
- Rotated files archived to `archive/YYYY/MM/DD/process_1/`
- Separate `error.log` sink for `ERROR+` only

### process_2 — Structured JSON Logging
- `serialize=True` — loguru outputs newline-delimited JSON (`.jsonl`)
- stdout JSON sink for live inspection
- `.jsonl` file sinks with archive rotation
- Each log line: `{"text": "...", "record": {"time": ..., "level": ..., "message": ...}}`

### process_3 — Exception Handling
- `@logger.catch` — decorator that catches and logs exceptions automatically
- `with logger.catch()` — context manager for scoped exception catching
- `logger.exception()` — manual try/except with full traceback
- `diagnose=True` — shows variable values inline inside tracebacks
- `backtrace=True` — full call stack on exceptions
- ~10% of logs trigger simulated exceptions (ValueError, KeyError, ConnectionError)

### process_4 — Binding and Context
- `logger.bind()` — attach static context fields to a logger instance per service
- `logger.contextualize()` — attach temporary context (job_id, user) for a request scope
- Per-service bound loggers: `pipeline_logger`, `auth_logger`, `dq_logger`, `system_logger`
- Message-prefix routing to correct bound logger

### process_5 — Async Logging
- `enqueue=True` — non-blocking thread-safe logging via internal queue
- 4 concurrent async workers via `asyncio.gather()`
- `logger.bind(worker=...)` — each worker tagged in every log line
- `await logger.complete()` — flushes all queued messages before exit

## Log Generators

| Generator | Level | Description |
|---|---|---|
| `make_http_log` | INFO/WARNING/ERROR | HTTP requests with status codes |
| `make_db_log` | INFO/WARNING | DB queries with duration |
| `make_auth_log` | INFO/WARNING | Login, logout, token events |
| `make_dq_log` | INFO/ERROR | Data quality check results |
| `make_pipeline_log` | INFO/ERROR | ETL pipeline stage events |
| `make_system_log` | INFO/WARNING/CRITICAL | CPU, memory, disk metrics |
| `make_error_log` | ERROR | Simulated exceptions |
| `make_debug_log` | DEBUG | Function execution traces |
| `make_warning_log` | WARNING | Deprecations, slow queries, rate limits |
| `make_alert_log` | CRITICAL | SLA breaches, memory leaks, brute force |

## Log Archive Structure

```
archive/
  YYYY/MM/DD/
    process_1/
      app_HHMMSS.log.gz
      error_HHMMSS.log.gz
    process_2/
      app_HHMMSS.jsonl.gz
      error_HHMMSS.jsonl.gz
    ...
```

## Environment Variables

| Variable | Default | Description |
|---|---|---|
| `LOG_PATH` | `logs` | Active log directory |
| `ARCHIVE_PATH` | `archive` | Rotated log archive root |

## Getting Started

```bash
uv sync
```

## Run a Process

```bash
uv run python process/process_1.py   # core plain logs
uv run python process/process_2.py   # JSON logging
uv run python process/process_3.py   # exception handling
uv run python process/process_4.py   # binding and context
uv run python process/process_5.py   # async logging
```

## Reusable Helpers

```python
# Add standard app + error file sinks for any process
from loguru_playground.config.logger_config import add_file_sinks
add_file_sinks("my_process", LOG_FORMAT, diagnose=True, backtrace=True)

# Infinite random log stream
from loguru_playground.generator.main import run_forever
for log in run_forever(interval_sec=0.5):
    logger.log(log["level"], log["message"])
```

## License

See [LICENSE](LICENSE) file for details.
