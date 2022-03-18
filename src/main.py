from typing import Optional
from fastapi.responses import HTMLResponse
import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="/app/templates/")

app.mount("/static", StaticFiles(directory="/app/static/"), name="static")


@app.get("/")
def read_root(request: Request):
    print(request.url_for("read_root"))
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        
        reload=True
        )