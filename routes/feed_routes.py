from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from util.templates import obter_jinja_templates

router = APIRouter(prefix="/feed")
templates = obter_jinja_templates("templates/feed")

@router.get("/home", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/feedhome.html", {"request": request})

@router.get("/demandasatendidas", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/demandasatendidas.html", {"request": request})

@router.get("/demandasnaoatendidas", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/demandasnaoatendidas.html", {"request": request})
