#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
[env]
# Conda Environment
conda create --name azure_fastapi python=3.9.13
conda info --envs
source activate azure_fastapi
conda deactivate

# if needed to remove
conda env remove -n [NAME_OF_THE_CONDA_ENVIRONMENT]
conda env remove -n azure_fastapi

# update conda 
conda update -n base -c defaults conda

# to export requirements
pip freeze > requirements.txt

# to install
pip install -r requirements.txt

# [path]
cd /Users/brunoflaven/Documents/03_git/ia_usages/ia_deploy_api_ml_architecture/fastapi_tiangolo_advanced_settings/

# LAUNCH THE API
ADMIN_EMAIL="tata@example.com" APP_NAME="monkeyApp" uvicorn main_3:app --reload

- requirements
pip install pydantic-settings

+ FastAPI Settings and Environment Variables
--- Source: https://fastapi.tiangolo.com/advanced/settings/


"""
from fastapi import FastAPI
from starlette.responses import RedirectResponse

# import the config from config_3.py
from config_3 import settings

app = FastAPI(
    title="TrattorIA",
    description="""EXAMPLE_3 Using config for FastAPI""",
    version="1.0",
    )

@app.get('/', include_in_schema=False)
def home():
    # return {"nlp_db_app - Welcome here - Benvenidos aqui - Добро пожаловать - Bienvenue ici"}
    return RedirectResponse(f"/docs")

@app.get("/info")
async def info():
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }




