"""
generator/main.py — Random log generator using Faker

Produces realistic plain-text log messages across multiple log types.
Each builder returns a dict with 'level' and 'message' keys.
Stream functions provide infinite or finite log generation.

Log types: http, database, auth, data_quality, pipeline, system, error, debug, alert, warning
"""

from faker import Faker
from typing import Callable
import random

fake = Faker()

# --- Level pickers ---

def pick_http_level(status: int) -> str:
    if status >= 500:
        return "ERROR"
    if status >= 400:
        return "WARNING"
    return "INFO"

def pick_dq_level(passed: bool) -> str:
    return "INFO" if passed else "ERROR"

# --- Log builders ---

def make_http_log() -> dict:
    status = random.choice([200, 201, 301, 400, 401, 403, 404, 500, 502, 503])
    method = random.choice(["GET", "POST", "PUT", "DELETE", "PATCH"])
    path = fake.uri_path()
    ip = fake.ipv4()
    duration = random.randint(10, 5000)
    user = fake.user_name()
    return {
        "level": pick_http_level(status),
        "message": f"{method} {path} {status} user={user} ip={ip} duration={duration}ms",
    }

def make_db_log() -> dict:
    duration = random.randint(1, 10000)
    query = random.choice(["SELECT", "INSERT", "UPDATE", "DELETE"])
    table = fake.word()
    rows = random.randint(0, 100000)
    return {
        "level": "WARNING" if duration > 5000 else "INFO",
        "message": f"DB {query} on {table} rows={rows} duration={duration}ms pool={random.randint(1, 20)}",
    }

def make_auth_log() -> dict:
    action = random.choice(["login_success", "login_failed", "logout", "token_expired", "unauthorized"])
    user = fake.email()
    ip = fake.ipv4()
    session = fake.uuid4()[:8]
    return {
        "level": "WARNING" if action in ("login_failed", "unauthorized") else "INFO",
        "message": f"AUTH {action} user={user} ip={ip} session={session}",
    }

def make_dq_log() -> dict:
    checks = ["null_check", "schema_check", "range_check", "duplicate_check", "referential_integrity"]
    passed = random.choices([True, False], weights=[80, 20])[0]
    check = random.choice(checks)
    table = f"{fake.word()}_{fake.word()}"
    rows_checked = random.randint(100, 1000000)
    rows_failed = 0 if passed else random.randint(1, 1000)
    status = "PASSED" if passed else "FAILED"
    return {
        "level": pick_dq_level(passed),
        "message": f"DQ {status} check={check} table={table} checked={rows_checked} failed={rows_failed}",
    }

def make_pipeline_log() -> dict:
    stage = random.choice(["extract", "transform", "load", "validate", "publish"])
    status = random.choices(["success", "failed", "skipped"], weights=[75, 15, 10])[0]
    pipeline = f"{fake.word()}_pipeline"
    records = random.randint(0, 500000)
    duration = random.randint(1, 3600)
    return {
        "level": "ERROR" if status == "failed" else "INFO",
        "message": f"PIPELINE {pipeline} stage={stage} status={status} records={records} duration={duration}s",
    }

def make_system_log() -> dict:
    cpu = random.uniform(0, 100)
    memory = random.uniform(0, 100)
    disk = random.uniform(0, 100)
    host = fake.hostname()
    level = "CRITICAL" if cpu > 95 or memory > 95 else "WARNING" if cpu > 80 or memory > 80 else "INFO"
    return {
        "level": level,
        "message": f"SYSTEM host={host} cpu={cpu:.1f}% mem={memory:.1f}% disk={disk:.1f}% conns={random.randint(0, 500)}",
    }

def make_error_log() -> dict:
    errors = [
        ("ValueError", "Invalid input data received"),
        ("KeyError", "Missing required field in payload"),
        ("ConnectionError", "Failed to connect to upstream service"),
        ("TimeoutError", "Request timed out after 30s"),
        ("PermissionError", "Insufficient permissions to access resource"),
        ("FileNotFoundError", "Required config file not found"),
        ("MemoryError", "Out of memory while processing batch"),
    ]
    exc_type, msg = random.choice(errors)
    module = f"{fake.word()}.{fake.word()}"
    line = random.randint(1, 500)
    return {
        "level": "ERROR",
        "message": f"EXCEPTION {exc_type} in {module}:{line} — {msg}",
    }

def make_debug_log() -> dict:
    fn = f"{fake.word()}_{fake.word()}"
    module = fake.word()
    duration = random.randint(1, 100)
    args = ", ".join(fake.word() for _ in range(random.randint(0, 3)))
    return {
        "level": "DEBUG",
        "message": f"DEBUG {module}.{fn}({args}) completed in {duration}ms",
    }

def make_warning_log() -> dict:
    warnings = [
        f"Deprecated API endpoint called by {fake.user_name()}",
        f"Slow query detected on table {fake.word()} — consider indexing",
        f"Retry attempt {random.randint(1, 5)} for job {fake.uuid4()[:8]}",
        f"Config value missing for {fake.word()}, using default",
        f"Rate limit approaching for ip={fake.ipv4()} — {random.randint(80, 99)}% used",
    ]
    return {
        "level": "WARNING",
        "message": f"WARNING {random.choice(warnings)}",
    }

def make_alert_log() -> dict:
    alerts = [
        f"ALERT cpu={random.uniform(95, 100):.1f}% on {fake.hostname()} — threshold exceeded",
        f"ALERT disk={random.uniform(90, 100):.1f}% on {fake.hostname()} — cleanup required",
        f"ALERT {random.randint(5, 50)} failed login attempts from ip={fake.ipv4()}",
        f"ALERT pipeline {fake.word()}_pipeline has been failing for {random.randint(2, 10)} consecutive runs",
        f"ALERT memory leak detected in {fake.word()}.{fake.word()} — usage growing {random.randint(1, 10)}MB/min",
        f"ALERT SLA breach — response time {random.randint(5000, 30000)}ms exceeds 3000ms threshold",
    ]
    return {
        "level": "CRITICAL",
        "message": random.choice(alerts),
    }

# --- Registry ---

LOG_BUILDERS: list[Callable[[], dict]] = [
    make_http_log,
    make_db_log,
    make_auth_log,
    make_dq_log,
    make_pipeline_log,
    make_system_log,
    make_error_log,
    make_debug_log,
    make_warning_log,
    make_alert_log,
]

# --- Stream generators ---

def log_stream(builder: Callable[[], dict], count: int):
    """Generate a fixed number of logs from a single builder."""
    return (builder() for _ in range(count))

def random_log_stream(count: int):
    """Generate a fixed number of logs from random builders."""
    return (random.choice(LOG_BUILDERS)() for _ in range(count))

def mixed_log_stream(count: int, weights: list[int] | None = None):
    """Generate a fixed number of logs with weighted builder selection."""
    return (random.choices(LOG_BUILDERS, weights=weights)[0]() for _ in range(count))

def run_forever(interval_sec: float = 0.5):
    """Yield random log dicts indefinitely. Stop with KeyboardInterrupt."""
    import time
    while True:
        yield random.choice(LOG_BUILDERS)()
        time.sleep(interval_sec)
