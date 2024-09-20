from fastapi import APIRouter, Form, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from models.usuario_model import Usuario


router = APIRouter(prefix="/usuario")

templates = Jinja2Templates(directory="templates")

