from app.core.rules import (
    has_fraud_indicators,
    is_fast_track,
    is_injury_claim
)


def route_claim(data: dict, missing_fields: list):
    description = data.get("description") or ""
    claim_type = data.get("claimType")
    estimated_damage = data.get("estimatedDamage")

    if has_fraud_indicators(description):
        return (
            "Investigation Flag",
            "Claim description contains potential fraud indicators."
        )

    if is_injury_claim(claim_type):
        return (
            "Specialist Queue",
            "Claim involves injury and requires specialist handling."
        )

    if missing_fields:
        return (
            "Manual Review",
            f"Missing mandatory fields: {', '.join(missing_fields)}."
        )
    
    if is_fast_track(estimated_damage):
        return (
            "Fast-track",
            f"Estimated damage is below ₹{25000}."
        )

    return (
        "Standard Processing",
        "All validations passed with no risk indicators."
    )
