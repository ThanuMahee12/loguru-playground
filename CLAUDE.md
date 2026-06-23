# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with this repository.

## Repository Purpose

A hands-on loguru exploration repo for data science and ML logging patterns. Each `loguru_playground/demo/process/process_N.py` script isolates a specific loguru feature using randomly generated fake logs.

## Stack

- **Python**: 3.13+
- **Package manager**: `uv`
- **Logging**: `loguru`
- **Fake data**: `faker`
- **Config**: `pyyaml`, `python-dotenv`
- **Versioning**: `hatch-vcs` (git tag driven)

## Project Structure

```
loguru_playground/
    config/
        env.py              # LOG_PATH, ARCHIVE_PATH as Path objects from .env
        logger.yaml         # per-process sink config (level, rotation, compression)
        logger_config.py    # add_file_sinks() and setup_logger() helpers
    demo/
        generator/
            main.py         # faker-based log generators, run_forever()
        process/
            process_1.py    # core plain logs + size rotation
            process_2.py    # structured JSON logging
            process_3.py    # exception handling — catch decorator, context manager, diagnose=True
            process_4.py    # binding and context — logger.bind, logger.contextualize
            process_5.py    # async logging — enqueue=True, concurrent workers
```

## Key Patterns

**Running a process:**
```bash
uv run python loguru_playground/demo/process/process_1.py
```

**Generator usage:**
```python
from loguru_playground.demo.generator.main import run_forever, random_log_stream
for log in run_forever(interval_sec=0.5):
    logger.log(log["level"], log["message"])
```

**Reusable file sinks:**
```python
from loguru_playground.config.logger_config import add_file_sinks
add_file_sinks("process_name", LOG_FORMAT, diagnose=True, backtrace=True)
```

## Log Archive Structure

```
archive/YYYY/MM/DD/<process>/app_HHMMSS.log.gz
archive/YYYY/MM/DD/<process>/error_HHMMSS.log.gz
```

## Branch Conventions

- Production: `main` (triggers auto-release via `.github/workflows/auto-release.yml`)
- Development: `staging`
- Feature branches: `feature/your-feature-name`

## Environment Variables

| Variable | Default | Description |
|---|---|---|
| `LOG_PATH` | `logs` | Active log directory |
| `ARCHIVE_PATH` | `archive` | Rotated log archive root |
