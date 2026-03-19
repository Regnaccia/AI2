from pydantic import BaseModel

from enum import Enum

class ProjectArea(str, Enum):
    SOFTWARE =  "software"
    HARDWARE = "hardware"