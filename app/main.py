from fastapi import FastAPI, UploadFile, File
from app.services.parser import extract_text
from app.services.extractor import extract_fields
from app.services.validator import find_missing_fields
from app.services.router import route_claim
from app.models.schemas import ClaimResponse

app = FastAPI(title="Autonomous Claims Agent")

@app.post("/process-claim", response_model=ClaimResponse)
def process_claim(file: UploadFile = File(...)):
    text = extract_text(file)
    extracted = extract_fields(text)
    missing = find_missing_fields(extracted)
    route, reason = route_claim(extracted, missing)

    return {
        "extractedFields": extracted,
        "missingFields": missing,
        "recommendedRoute": route,
        "reasoning": reason
    }
