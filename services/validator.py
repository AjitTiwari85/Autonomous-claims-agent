from app.core.config import MANDATORY_FIELDS

def find_missing_fields(data: dict) -> list:
    return [f for f in MANDATORY_FIELDS if not data.get(f)]
