from core.contracts.models import AgentResult, ValidationFeedback


class EditalValidator:
    name = "validador-edital"

    def validate(self, result: AgentResult) -> ValidationFeedback:
        errors = []
        if result.status.value == "ATENDE" and not result.evidence_ids:
            from core.contracts.models import ValidationErrorItem
            errors.append(
                ValidationErrorItem(
                    code="MISSING_EVIDENCE",
                    severity="HIGH",
                    requirement_id=result.requirement_id,
                    description="Resultado ATENDE sem evidência vinculada.",
                    correction="Adicionar evidência ou rever o status.",
                )
            )
        return ValidationFeedback(
            validation="REJECTED" if errors else "APPROVED",
            errors=errors,
            retry_allowed=bool(errors),
            target_agent="agente-edital",
        )
