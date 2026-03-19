from pydantic import BaseModel, Field
from models.log import Log

class LogRegistry(BaseModel):
    logs: list[Log] = Field(default=[])

    def add_log(self, kind, sender,send_to,context,generate_task=False,task=""):
        log = Log(
            kind= kind,
            sender= sender,
            send_to= send_to,
            context= context,
            generate_task= generate_task,
            task= task
        )
        self.logs.append(log)