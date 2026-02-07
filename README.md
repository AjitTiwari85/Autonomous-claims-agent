# Autonomous Insurance Claims Processing Agent

Lightweight backend agent that ingests FNOL (First Notice of Loss) documents, extracts structured data, validates completeness, and routes the claim to the appropriate processing workflow.

---

## Problem Summary

The system must:

- Extract key insurance claim fields from PDF/TXT documents  
- Identify missing or inconsistent information  
- Apply routing rules  
- Provide explainable reasoning for the decision  

---

## Approach

The solution is built using a modular, production-style architecture.

### Pipeline

Document → Parser → Extractor → Validator → Router → JSON Output

### Key Design Principles

- Separation of concerns  
- Reusable utilities  
- Deterministic rule engine  
- Defensive data validation  
- Explainable outputs  

---

## Components

### Parser
Reads PDF/TXT and converts to raw text.

### Extractor
Uses regex + heuristics to detect fields.

To avoid incorrect captures from templates (e.g. labels instead of filled values),  
the system filters suspicious values like:

- ALL CAPS headings  
- Instruction text in brackets  
- Common form words (address, contact, etc.)

If confidence is low → value becomes `null`.

### Validator
Checks mandatory fields and builds missing list.

### Router
Applies business rules in priority order:

1. Fraud keywords → Investigation  
2. Injury → Specialist  
3. Missing info → Manual Review  
4. Low damage → Fast-track  
5. Otherwise → Standard Processing

### Explainability
Every routing decision includes a human-readable reason.

---

## ⚙ Tech Stack

- Python
- FastAPI
- Uvicorn
- Regex-based extraction

---

## ▶ Steps to Run

### 1. Clone repository

```bash
git clone <repo-url>
cd autonomous-claims-agent
```
2. Create virtual environment
   python -m venv venv
   
   Activate:
   Windows
   venv\Scripts\activate

   Mac/Linux
   source venv/bin/activate
   
3. Install dependencies
   pip install -r requirements.txt

4. Start server
   uvicorn app.main:app --reload
   
5. Open API docs
   http://127.0.0.1:8000/docs

   Upload FNOL file → Execute

6.Example Output
   {
  "extractedFields": {},
  "missingFields": [],
  "recommendedRoute": "Manual Review",
  "reasoning": "Mandatory information missing."
}

## Assumptions & Notes

- Sample ACORD files are mostly templates; many values may be absent.
- The system prioritizes data integrity over guessing.
- If extraction is uncertain → field is marked missing.

## Possible Future Improvements

- LLM-based extraction fallback
- Confidence scoring
- OCR for scanned PDFs
- ML classification for routing

👨‍💻 Author
   Ajit Tiwari

