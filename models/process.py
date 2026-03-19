from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ProcessConfig:
    """Definisce la struttura delle specifiche di un processo"""
    process_name: str
    agent_role: str
    agent_tools: List[str]

class ProcessSpec:
    # Definiamo le specifiche come istanze della dataclass
    INGEST = ProcessConfig(
        process_name="ingest",
        agent_role="Agent_1",
        agent_tools=["T1", "T2"]
    )
    
    ANALIZE = ProcessConfig(
        process_name="analize",
        agent_role="Agent_2",
        agent_tools=[]
    )

    # Creiamo un mapping per la ricerca rapida
    _registry = {
        INGEST.process_name: INGEST,
        ANALIZE.process_name: ANALIZE
    }

    @classmethod
    def get_by_process_name(cls, name: str) -> Optional[ProcessConfig]:
        return cls._registry.get(name)

if __name__ == "__main__":
    # Esempio di utilizzo
    spec = ProcessSpec.get_by_process_name("ingest")
    if spec:
        print(f"Role: {spec.agent_role}, Tools: {spec.agent_tools}")