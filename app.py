from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, JSONResponse
from contextlib import asynccontextmanager
from textSummarizer.pipeline.prediction import PredictionPipeline

pipeline_obj = None

@asynccontextmanager
async def lifespan(app):
    global pipeline_obj
    print("⏳ Model load ho raha hai...")
    pipeline_obj = PredictionPipeline()
    print("✅ Model ready!")
    yield

app = FastAPI(lifespan=lifespan)
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home():
    return RedirectResponse(url="/ui")

@app.get("/ui")
def ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
def predict(text: str = Form(...)):
    summary = pipeline_obj.predict(text)
    return JSONResponse({"summary": summary})  # ✅ JSON return