# main.py
from fastapi import FastAPI
from routers import matches  # আমাদের বানানো রাউটার ইমপোর্ট করলাম

app = FastAPI(title="Media Content Management API")

# রাউটারটিকে মেইন অ্যাপের সাথে যুক্ত করা হলো
app.include_router(matches.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Media API Server"}