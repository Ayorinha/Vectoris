"""Retrieval evaluation with explicit relevance labels."""
from dataclasses import dataclass
from .metrics import reciprocal_rank

@dataclass(frozen=True)
class RetrievalCase:
    query: str
    relevance: tuple[int, ...]

def evaluate(cases: list[RetrievalCase]) -> dict[str, float]:
    if not cases: raise ValueError("cases must not be empty")
    mrr = sum(reciprocal_rank(list(case.relevance)) for case in cases) / len(cases)
    return {"mrr": mrr, "cases": float(len(cases))}