"""
logger_config.py — Dynamic loguru setup from logger.yaml

Loads per-process sink configuration from logger.yaml and applies it
to loguru. Each process gets isolated sinks with its own rotation,
retention, and format settings.

Usage:
    from loguru_playground.config.logger_config import setup_logger, add_file_sinks
    setup_logger("process_1")
    add_file_sinks("process_3", LOG_FORMAT, diagnose=True, backtrace=True)
"""

import sys
from pathlib import Path
import yaml
from loguru import logger
from loguru_playground.config.env import ARCHIVE_PATH

CONFIG_PATH = Path(__file__).parent / "logger.yaml"


def _load_config() -> dict:
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)


def _add_sink(sink_name: str, sink_cfg: dict) -> None:
    if sink_name == "stdout":
        logger.add(
            sys.stdout,
            level=sink_cfg.get("level", "DEBUG"),
            format=sink_cfg.get("format", "{time} | {level} | {message}"),
            colorize=sink_cfg.get("colorize", False),
            serialize=sink_cfg.get("serialize", False),
        )
    else:
        path = Path(sink_cfg["path"])
        path.parent.mkdir(parents=True, exist_ok=True)

        kwargs = {
            "level": sink_cfg.get("level", "DEBUG"),
            "serialize": sink_cfg.get("serialize", False),
        }

        if not sink_cfg.get("serialize", False):
            kwargs["format"] = sink_cfg.get("format", "{time} | {level} | {message}")

        if "rotation" in sink_cfg:
            kwargs["rotation"] = sink_cfg["rotation"]
        if "retention" in sink_cfg:
            kwargs["retention"] = sink_cfg["retention"]
        if "compression" in sink_cfg:
            kwargs["compression"] = sink_cfg["compression"]

        logger.add(path, **kwargs)


def add_file_sinks(
    process_name: str,
    log_format: str,
    diagnose: bool = False,
    backtrace: bool = False,
) -> None:
    """Add standard app + error file sinks for a process with archive rotation."""
    common = {
        "format": log_format,
        "rotation": "20 KB",
        "compression": "gz",
        "diagnose": diagnose,
        "backtrace": backtrace,
    }
    logger.add(
        str(ARCHIVE_PATH / "{time:YYYY/MM/DD}" / process_name / "app_{time:HHmmss}.log"),
        level="DEBUG",
        retention=5,
        **common,
    )
    logger.add(
        str(ARCHIVE_PATH / "{time:YYYY/MM/DD}" / process_name / "error_{time:HHmmss}.log"),
        level="ERROR",
        retention=3,
        **common,
    )


def setup_logger(process_name: str) -> None:
    """Configure loguru sinks for the given process from logger.yaml."""
    config = _load_config()

    if process_name not in config:
        raise ValueError(f"Process '{process_name}' not found in logger.yaml")

    logger.remove()

    process_cfg = config[process_name]
    for sink_name, sink_cfg in process_cfg["sinks"].items():
        _add_sink(sink_name, sink_cfg)

    logger.info(f"Logger configured for {process_name}: {process_cfg.get('description', '')}")
