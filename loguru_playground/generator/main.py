from faker import Faker
from typing import Callable
import random

fake = Faker()

# --- Log level picker ---

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
    return {
        "type": "http",
        "level": pick_http_level(status),
        "ip": fake.ipv4(),
        "user": fake.user_name(),
        "method": random.choice(["GET", "POST", "PUT", "DELETE", "PATCH"]),
        "path": fake.uri_path(),
        "status": status,
        "response_time_ms": random.randint(10, 5000),
        "user_agent": fake.user_agent(),
    }

def make_db_log() -> dict:
    duration = random.randint(1, 10000)
    return {
        "type": "database",
        "level": "WARNING" if duration > 5000 else "INFO",
        "query": random.choice(["SELECT", "INSERT", "UPDATE", "DELETE"]),
        "table": fake.word(),
        "duration_ms": duration,
        "rows_affected": random.randint(0, 100000),
        "connection_pool": random.randint(1, 20),
    }

def make_auth_log() -> dict:
    action = random.choice(["login_success", "login_failed", "logout", "token_expired", "unauthorized"])
    return {
        "type": "auth",
        "level": "WARNING" if action in ("login_failed", "unauthorized") else "INFO",
        "user": fake.email(),
        "action": action,
        "ip": fake.ipv4(),
        "session_id": fake.uuid4(),
    }

def make_dq_log() -> dict:
    checks = ["null_check", "schema_check", "range_check", "duplicate_check", "referential_integrity"]
    passed = random.choices([True, False], weights=[80, 20])[0]
    return {
        "type": "data_quality",
        "level": pick_dq_level(passed),
        "dataset": fake.word(),
        "check": random.choice(checks),
        "passed": passed,
        "rows_checked": random.randint(100, 1000000),
        "rows_failed": 0 if passed else random.randint(1, 1000),
        "table": f"{fake.word()}_{fake.word()}",
    }

def make_pipeline_log() -> dict:
    stage = random.choice(["extract", "transform", "load", "validate", "publish"])
    status = random.choices(["success", "failed", "skipped"], weights=[75, 15, 10])[0]
    return {
        "type": "pipeline",
        "level": "ERROR" if status == "failed" else "INFO",
        "pipeline": f"{fake.word()}_pipeline",
        "stage": stage,
        "status": status,
        "records_processed": random.randint(0, 500000),
        "duration_sec": random.randint(1, 3600),
    }

def make_system_log() -> dict:
    cpu = random.uniform(0, 100)
    memory = random.uniform(0, 100)
    return {
        "type": "system",
        "level": "CRITICAL" if cpu > 95 or memory > 95 else "WARNING" if cpu > 80 or memory > 80 else "INFO",
        "host": fake.hostname(),
        "cpu_percent": round(cpu, 2),
        "memory_percent": round(memory, 2),
        "disk_percent": round(random.uniform(0, 100), 2),
        "open_connections": random.randint(0, 500),
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
    return {
        "type": "error",
        "level": "ERROR",
        "exception": exc_type,
        "message": msg,
        "module": f"{fake.word()}.{fake.word()}",
        "line": random.randint(1, 500),
        "user": fake.user_name(),
    }

def make_debug_log() -> dict:
    return {
        "type": "debug",
        "level": "DEBUG",
        "function": f"{fake.word()}_{fake.word()}",
        "module": fake.word(),
        "args": [fake.word() for _ in range(random.randint(0, 3))],
        "execution_time_ms": random.randint(1, 100),
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
]

# --- Stream generators ---

def log_stream(builder: Callable[[], dict], count: int):
    return (builder() for _ in range(count))

def random_log_stream(count: int):
    return (random.choice(LOG_BUILDERS)() for _ in range(count))

def mixed_log_stream(count: int, weights: list[int] | None = None):
    return (random.choices(LOG_BUILDERS, weights=weights)[0]() for _ in range(count))
