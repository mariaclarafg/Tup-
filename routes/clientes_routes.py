from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from util.templates import obter_jinja_templates

router = APIRouter(prefix="/cliente")
templates = obter_jinja_templates("templates/cliente")

@router.get("/centroPessoal/perfil", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/centroPessoal/perfil.html", {"request": request})