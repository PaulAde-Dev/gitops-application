from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/healthz")
def health():
    return {"status": "healthy"}

@app.get("/readyz")
def ready():
    return {"status": "ready"}
