# loguru-playground

A hands-on exploration of loguru's logging capabilities for data pipelines and ML workflows.

## Overview

This repo explores loguru features through isolated process scripts, each covering a specific logging pattern. Random log data is generated using `faker` to simulate realistic data science and ML workloads.

## Project Structure

```
loguru_playground/
    config/
        env.py              # LOG_PATH, ARCHIVE_PATH globals
        logger.yaml         # per-process sink configuration
        logger_config.py    # dynamic logger setup from yaml
    generator/
        main.py             # random log generator (faker)
process/
    process_1.py            # core plain text logging + size rotation
    process_2.py            # structured JSON logging
```

## Processes

| Process | Feature |
|---|---|
| `process_1.py` | Core plain logs, size-based rotation, archive path |
| `process_2.py` | Structured JSON logging (`.jsonl`), archive rotation |

## Log Output

Rotated logs are archived to:
```
archive/YYYY/MM/DD/<process>/app_HHMMSS.log.gz
archive/YYYY/MM/DD/<process>/error_HHMMSS.log.gz
```

## Getting Started

```bash
uv sync
```

## Run a Process

```bash
uv run python process/process_1.py
uv run python process/process_2.py
```

## License

See [LICENSE](LICENSE) file for details.
