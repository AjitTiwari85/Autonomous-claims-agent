from app.utils.helpers import safe_search, to_int, is_valid_value


def extract_fields(text: str) -> dict:
    data = {}

    # Policy Number
    value = safe_search(r"Policy Number[:\s]+(.+)", text)
    data["policyNumber"] = value if is_valid_value(value) else None

    # Policyholder Name
    value = safe_search(r"Name of Insured[:\s]+(.+)", text)
    data["policyholderName"] = value if is_valid_value(value) else None

    # Incident Date
    value = safe_search(r"Date of Loss[:\s]+(.+)", text)
    data["incidentDate"] = value if is_valid_value(value) else None

    # Location
    value = safe_search(r"Location of Loss[:\s]+(.+)", text)
    data["location"] = value if is_valid_value(value) else None

    # Description
    value = safe_search(r"Description of Accident[:\s]+(.+)", text)
    data["description"] = value if is_valid_value(value) else None

    # Estimated Damage
    value = safe_search(r"Estimate Amount[:\s]+(.+)", text)
    value = value if is_valid_value(value) else None
    data["estimatedDamage"] = to_int(value)

    # Claim type heuristic
    data["claimType"] = "injury" if "injur" in text.lower() else "vehicle"

    # initial estimate
    data["initialEstimate"] = data["estimatedDamage"]

    return data
