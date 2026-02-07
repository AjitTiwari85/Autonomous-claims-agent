from app.core.config import DAMAGE_THRESHOLD, FRAUD_KEYWORDS

def route_claim(data: dict, missing_fields: list):
    description = (data.get("description") or "").lower()

    if any(word in description for word in FRAUD_KEYWORDS):
        return "Investigation Flag", "Suspicious keywords detected in description"

    if data.get("claimType") == "injury":
        return "Specialist Queue", "Injury-related claim"

    if missing_fields:
        return "Manual Review", "Mandatory fields missing"

    if data.get("estimatedDamage", 0) < DAMAGE_THRESHOLD:
        return "Fast-track", "Estimated damage below threshold"

    return "Standard Processing", "All checks passed"
