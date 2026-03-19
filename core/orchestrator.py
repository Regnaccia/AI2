from models.log import Log

def start_new_project(log_reg):
    print("Starting new project")
    print("enter yoour prompt")
    text = input("->")

    log_reg.add_log(
            kind="user_prompt",
            sender= "user",
            send_to= "agent_1",
            context= {
                "prompt" : text
            },
            generate_task= True,
            task= "ingest"
        )

def Run(log_reg):
    last_log = ""
    while True:
        if last_log == "":
            start_new_project(log_reg)
        
        last_log = log_reg.logs[-1]
        if last_log.generate_task == True:
            print("task")
            break

