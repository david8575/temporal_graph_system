from fastapi import FastAPI
from app.routes import graph_router

app = FastAPI()
app.include_router(graph_router)

@app.get("/")
def root():
    return {"message": "temporal graph api running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)