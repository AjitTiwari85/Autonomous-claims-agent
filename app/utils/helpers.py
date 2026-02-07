import re


def safe_search(pattern: str, text: str):
    match = re.search(pattern, text, re.IGNORECASE)
    return match.group(1).strip() if match else None


def to_int(value: str):
    if not value:
        return None
    try:
        return int(value.replace(",", "").strip())
    except ValueError:
        return None

def is_valid_value(value: str):
    if not value:
        return False

    value = value.strip()

    # too big → heading
    if len(value) > 60:
        return False

    # all caps → label
    if value.isupper():
        return False

    # contains instruction brackets
    if "(" in value and ")" in value:
        return False

    # common form words
    blacklist = [
        "address",
        "contact",
        "phone",
        "department",
        "policyholder",
        "insured",
        "mailing"
    ]

    if any(word in value.lower() for word in blacklist):
        return False

    return True
