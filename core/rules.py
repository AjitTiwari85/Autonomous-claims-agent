from app.core.config import DAMAGE_THRESHOLD, FRAUD_KEYWORDS


def has_fraud_indicators(description: str) -> bool:
    if not description:
        return False
    description = description.lower()
    return any(word in description for word in FRAUD_KEYWORDS)


def is_fast_track(estimated_damage: int) -> bool:
    if estimated_damage is None:
        return False
    return estimated_damage < DAMAGE_THRESHOLD


def is_injury_claim(claim_type: str) -> bool:
    if not claim_type:
        return False
    return claim_type.lower() == "injury"
