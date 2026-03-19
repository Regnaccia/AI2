from typing import Any

from pydantic import BaseModel, Field, model_validator
from uuid import uuid4

from models.process import ProcessSpec, ProcessConfig

class Log(BaseModel):
    log_id:     str = Field(default_factory=lambda: f"log_{uuid4()}")
    kind:       str
    sender:     str
    process:    ProcessConfig
    send_to:    str = Field(default="None") 
    context:    dict = Field(default= {}) 

    @model_validator(mode='after')
    def set_send_to(self) -> 'Log':
        if self.send_to is "None":
            self.send_to = self.process.agent_role
        return self


if __name__ == "__main__":
      l =Log(
            kind= "test",
            sender= "user",
            process= ProcessSpec.INGEST,
            context={
                  "text" : "this is a test"
            },            
      )
      
      print(l.model_dump_json(indent=4))
    
