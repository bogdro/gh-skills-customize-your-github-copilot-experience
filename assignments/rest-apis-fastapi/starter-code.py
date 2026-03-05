from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Task Management API"}

# TODO: Add task management endpoints here