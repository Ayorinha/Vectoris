from __future__ import annotations
from dataclasses import dataclass
import math
@dataclass(frozen=True, slots=True)
class Vector:
    id: str; values: tuple[float, ...]
    def __post_init__(self):
        if not self.id or not self.values: raise ValueError("id and vector values are required")
class InMemoryVectorIndex:
    def __init__(self): self._items: list[Vector] = []
    def add(self, vector: Vector) -> None:
        if self._items and len(vector.values) != len(self._items[0].values): raise ValueError("dimension mismatch")
        self._items.append(vector)
    def search(self, query: tuple[float, ...], *, k: int = 5) -> list[tuple[str, float]]:
        if k < 1: raise ValueError("k must be positive")
        if self._items and len(query) != len(self._items[0].values): raise ValueError("dimension mismatch")
        def cosine(v: Vector) -> float:
            den = math.sqrt(sum(x*x for x in query)) * math.sqrt(sum(x*x for x in v.values))
            return sum(a*b for a,b in zip(query, v.values)) / den if den else 0.0
        return [(v.id, cosine(v)) for v in sorted(self._items, key=cosine, reverse=True)[:k]]
