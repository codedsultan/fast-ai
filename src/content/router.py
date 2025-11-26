from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_content():
    return {"message": "content module ok"}
