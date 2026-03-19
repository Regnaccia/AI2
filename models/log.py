from typing import Any

from pydantic import BaseModel, Field
from uuid import uuid4


class Log(BaseModel):
    log_id:     str = Field(default_factory=lambda: f"log_{uuid4()}")
    kind:       str
    sender:     str
    send_to:    str
    context:    dict = Field(default= {}) 
    generate_task : bool = Field(default=False)
    task: str = Field(default="")

if __name__ == "__main__":
      l =Log(
            kind= "test",
            sender= "user",
            send_to= "test",
            context={
                  "text" : "this is a test"
            },
            generate_task=True
            
      )
      
      print(l.model_dump_json(indent=4))
    
