from fastapi import FastAPI

app = FastAPI(title="FastAPI CI/CD Example")

@app.get("/")
def home():
    return {"message": "FastAPI app running in Docker!"}
