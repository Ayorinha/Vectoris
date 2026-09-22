"""Retrieval quality metrics with explicit validation."""
import math

def reciprocal_rank(relevance: list[int]) -> float:
    for i, value in enumerate(relevance, 1):
        if value:
            return 1.0 / i
    return 0.0

def dcg(relevance: list[float]) -> float:
    return sum((2**rel - 1) / math.log2(i + 2) for i, rel in enumerate(relevance))
