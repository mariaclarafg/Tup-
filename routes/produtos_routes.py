from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from util.templates import obter_jinja_templates

router = APIRouter(prefix="/produtos")
templates = obter_jinja_templates("templates/produtos")




@router.get("/detalhes", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/produtoDetalhes.html", {"request": request})