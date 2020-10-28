import os
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseSettings
from h1st.model_repository.explorer import ModelExplorer


class Settings(BaseSettings):
    project_root: str = os.getcwd()


settings = Settings()
app = FastAPI()


@app.get("/api/models")
def get_models() -> dict:
    explorer = ModelExplorer(settings.project_root)
    models = explorer.discover_models()
    return {
        "items": list(models.values())
    }

@app.post('/api/tune')
def start_tune() -> dict:
    pass
