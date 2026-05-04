# routers/matches.py
from fastapi import APIRouter, HTTPException, Depends
from schemas import MatchSchema
from dummy_db import matches_db
from dependencies import verify_api_key 
router = APIRouter(
    prefix="/matches",
    tags=["Matches API"]
)

@router.get("/", dependencies=[Depends(verify_api_key)])
async def get_all_matches():
    return {"total_matches": len(matches_db), "data": matches_db}

@router.get("/{match_id}")
async def get_single_match(match_id: int):
    for match in matches_db:
        if match["id"] == match_id:
            return match
    raise HTTPException(status_code=404, detail="Match not found!")

@router.post("/", dependencies=[Depends(verify_api_key)])
async def add_new_match(new_match: MatchSchema):
    matches_db.append(new_match.model_dump())
    return {"message": "Match added successfully!", "match_info": new_match}
