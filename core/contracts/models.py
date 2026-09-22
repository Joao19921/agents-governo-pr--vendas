from enum import Enum
from pydantic import BaseModel, Field


class AnalysisStatus(str, Enum):
    ATENDE = "ATENDE"
    ATENDE_PARCIALMENTE = "ATENDE_PARCIALMENTE"
    NAO_ATENDE = "NAO_ATENDE"
    NAO_COMPROVADO = "NAO_COMPROVADO"
    NECESSITA_DILIGENCIA = "NECESSITA_DILIGENCIA"


class SourceRef(BaseModel):
    document_id: str
    page: int | None = None
    excerpt: str | None = None


class Requirement(BaseModel):
    requirement_id: str
    category: str
    description: str
    mandatory: bool
    source: SourceRef


class Evidence(BaseModel):
    evidence_id: str
    document_id: str
    page: int | None = None
    excerpt: str | None = None
    extracted_fields: dict[str, object] = Field(default_factory=dict)
    extraction_method: str


class AgentResult(BaseModel):
    requirement_id: str
    status: AnalysisStatus
    evidence_ids: list[str] = Field(default_factory=list)
    justification: str
    agent_name: str
    agent_version: str


class ValidationErrorItem(BaseModel):
    code: str
    severity: str
    requirement_id: str | None = None
    description: str
    expected: object | None = None
    found: object | None = None
    correction: str


class ValidationFeedback(BaseModel):
    validation: str
    errors: list[ValidationErrorItem] = Field(default_factory=list)
    retry_allowed: bool
    target_agent: str
