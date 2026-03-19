from models.log import Log
from models.process import ProcessSpec

def start_new_project(log_reg):
    print("Starting new project")
    print("enter yoour prompt")
    text = input("->")

    log_reg.add_log(
            kind="user_prompt",
            sender= "user",
            process= ProcessSpec.INGEST,
            context= {
                "prompt" : text
            },
        )

def Run(log_reg):
    last_log = ""
    while True:
        if last_log == "":
            start_new_project(log_reg)
            print(log_reg)
            break
        
        

