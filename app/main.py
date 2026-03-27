from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .engine import humanize_text
from .stats import calculate_stats

app = FastAPI(title="Antigravity AI Humanizer API")

# Enable CORS for frontend interaction
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class HumanizeRequest(BaseModel):
    text: str

class HumanizeResponse(BaseModel):
    original_text: str
    humanized_text: str
    stats: dict

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/humanize", response_model=HumanizeResponse)
async def humanize(request: HumanizeRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text is required")
    
    try:
        # Get humanized text from LLM
        humanized = await humanize_text(request.text)
        
        # Calculate stats for the humanized result
        stats = calculate_stats(humanized)
        
        return {
            "original_text": request.text,
            "humanized_text": humanized,
            "stats": stats
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
