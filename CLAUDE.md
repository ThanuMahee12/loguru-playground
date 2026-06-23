# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with this repository.

## Repository Purpose

A hands-on loguru exploration repo for data science and ML logging patterns. Each `process/process_N.py` script isolates a specific loguru feature using randomly generated fake logs.

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
        logger_config.py    # setup_logger(process_name) reads logger.yaml
    generator/
        main.py             # faker-based log generators, run_forever()
process/
    process_1.py            # core plain logs + size rotation
    process_2.py            # structured JSON logging
    process_3.py            # exception handling — catch decorator, context manager, diagnose=True
```

## Key Patterns

**Running a process:**
```bash
uv run python process/process_1.py
```

**Generator usage:**
```python
from loguru_playground.generator.main import run_forever, random_log_stream
for log in run_forever(interval_sec=0.5):   # infinite
    logger.log(log["level"], log["message"])
```

**Dynamic logger setup:**
```python
from loguru_playground.config.logger_config import setup_logger
setup_logger("process_1")  # reads sinks from logger.yaml
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
