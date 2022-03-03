# Import Packages
from typing import Optional
from fastapi import FastAPI, APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from starlette.responses import RedirectResponse
from jwt_token import get_token
from sqlalchemy.orm import Session
from database import get_db
from oauth2 import hasAccess
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware


# Import Models
from models import *


app = FastAPI()

# Template
template = Jinja2Templates(directory = "app/internal/logistics/am/templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Authorization
AUTHORIZED_SUBSYSTEM = "Asset Management"
AUTHORIZED_ROLE = "Equipment Manager"




# ===========================================================
# WEB ROUTES
# ===========================================================


# Redirect if url is blank
@app.get("/asset_management/manager", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/equipment_manager/dashboard.html", {"request": request})

@app.get("/asset_management/manager/requests", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/equipment_manager/request_assets.html", {"request": request})

@app.get("/asset_management/manager/asset_type", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/equipment_manager/asset_type.html", {"request": request})

@app.get("/asset_management/manager/asset_provider", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/equipment_manager/asset_provider.html", {"request": request})

@app.get("/asset_management/manager/asset", response_class=HTMLResponse)
def get_asset(request: Request,):
    return template.TemplateResponse("asset_management/equipment_manager/asset.html", {"request": request})

@app.get("/asset_management/manager/asset/view/{id}", response_class=HTMLResponse)
def get_asset(request: Request, id: str):
    return template.TemplateResponse("asset_management/equipment_manager/asset_view.html", {"request": request, "id": id})

@app.get("/asset_management/manager/maintenance_provider", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/equipment_manager/maintenance_provider.html", {"request": request})

@app.get("/asset_management/manager/maintenance_page", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/equipment_manager/maintenance_page.html", {"request": request})