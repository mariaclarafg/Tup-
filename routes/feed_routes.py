from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from util.templates import obter_jinja_templates

router = APIRouter(prefix="/feed")
templates = Jinja2Templates(directory="templates")


@router.get("/demandasatendidas", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("feed/pages/demandasatendidas.html", {"request": request})

@router.get("/demandasnaoatendidas", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("feed/pages/demandasnaoatendidas.html", {"request": request})
