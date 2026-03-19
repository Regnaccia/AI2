from typing import Any

from pydantic import BaseModel, Field, model_validator
from uuid import uuid4

from models.process import ProcessSpec, ProcessConfig

class Task(BaseModel):
    pass

    