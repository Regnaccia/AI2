
from models.log_reg import LogRegistry

from core.orchestrator import Run

if __name__ == "__main__":
    # start log registry
    log_reg = LogRegistry()

Run(log_reg)

        



