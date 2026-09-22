from core.contracts.models import AgentResult


class EditalExecutor:
    name = "agente-edital"
    version = "0.1.0"

    def execute(self, requirement_id: str, justification: str) -> AgentResult:
        raise NotImplementedError
