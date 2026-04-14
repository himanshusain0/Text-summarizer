from fastapi import FastAPI
import uvicorn
import os
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from pydantic import BaseModel

from textSummarizer.pipeline.prediction import PredictionPipeline

app = FastAPI()

# ✅ Request Body Model (IMPORTANT FIX)
class TextRequest(BaseModel):
    text: str


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful !!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")


@app.post("/predict")
async def predict_route(request: TextRequest):
    try:
        obj = PredictionPipeline()
        result = obj.predict(request.text)
        return {"summary": result}
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

# from fastapi import FastAPI, Form, Request
# from fastapi.templating import Jinja2Templates
# from fastapi.responses import RedirectResponse
# from textSummarizer.pipeline.prediction import PredictionPipeline

# app = FastAPI()
# templates = Jinja2Templates(directory="templates")

# @app.get("/")
# def home():
#     return RedirectResponse(url="/ui")

# @app.get("/ui")
# def ui(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

# @app.post("/predict")
# def predict(text: str = Form(...)):
#     obj = PredictionPipeline()
#     return obj.predict(text)