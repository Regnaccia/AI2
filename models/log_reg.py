from pydantic import BaseModel, Field
from models.log import Log

class LogRegistry(BaseModel):
    logs: list[Log] = Field(default=[])

    def add_log(self, kind, sender,process,context):
        log = Log(
            kind= kind,
            sender= sender,
            process = process,
            context= context
        )
        self.logs.append(log)