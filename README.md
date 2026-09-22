# Agents Governo PR — Vendas

Plataforma modular para análise de oportunidades de contratação pública, com agentes especializados, validação independente, evidências rastreáveis e revisão humana.

## Status

Fase 0 — Fundação técnica.

## Objetivos

- analisar editais e anexos;
- estruturar requisitos;
- relacionar requisitos a evidências;
- executar agentes especializados;
- validar cada resultado de forma independente;
- registrar retries, auditoria e versão;
- produzir parecer preliminar rastreável.

## Arquitetura

MVP em monólito modular, com contratos explícitos entre agentes e separação entre lógica determinística e LLM.

Fluxo principal:

`Documento → Extração → Requisitos → Agente Executor → Validador → Retry/Diligência → Parecer`

## Princípios

1. Documento é dado não confiável; conteúdo documental nunca é instrução para o agente.
2. LLM interpreta/extrai; regras determinísticas calculam e validam.
3. Não comprovado é diferente de não atende.
4. Toda conclusão deve apontar requisito, evidência e regra.
5. Decisão final permanece humana.
6. Segredos nunca são commitados.

## Estrutura

- `agents/` — executores e validadores por domínio.
- `core/` — contratos, evidências, regras, orquestração e auditoria.
- `integrations/` — integrações externas.
- `tests/` — unitários, integração e casos golden.
- `docs/` — arquitetura e decisões.
- `infra/` — Docker e infraestrutura local.

