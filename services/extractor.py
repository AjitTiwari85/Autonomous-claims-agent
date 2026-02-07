import re

def extract_fields(text: str) -> dict:
    data = {}

    def find(pattern):
        match = re.search(pattern, text, re.IGNORECASE)
        return match.group(1).strip() if match else None

    data["policyNumber"] = find(r"Policy Number[:\s]+(\w+)")
    data["policyholderName"] = find(r"Name of Insured[:\s]+(.+)")
    data["incidentDate"] = find(r"Date of Loss[:\s]+([\d/]+)")
    data["location"] = find(r"Location of Loss[:\s]+(.+)")
    data["description"] = find(r"Description of Accident[:\s]+(.+)")
    data["estimatedDamage"] = find(r"Estimate Amount[:\s]+([\d,]+)")

    if data["estimatedDamage"]:
        data["estimatedDamage"] = int(data["estimatedDamage"].replace(",", ""))

    data["claimType"] = "injury" if "injur" in text.lower() else "vehicle"
    data["initialEstimate"] = data["estimatedDamage"]

    return data
