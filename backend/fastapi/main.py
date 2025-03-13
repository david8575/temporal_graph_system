from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import graph_router

app = FastAPI()
app.include_router(graph_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "temporal graph api running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)