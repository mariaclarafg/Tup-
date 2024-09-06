from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from util.templates import obter_jinja_templates

router = APIRouter(prefix="/gruposecomunidades")
templates = obter_jinja_templates("templates/gruposcomunidades")

@router.get("/bordadeiras", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/bordadeiras.html", {"request": request})