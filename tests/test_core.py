from vectoris.core import InMemoryVectorIndex, Vector

def test_similarity_search():
    i = InMemoryVectorIndex(); i.add(Vector("a", (1.0, 0.0))); i.add(Vector("b", (0.0, 1.0)))
    assert i.search((1.0, 0.0), k=1) == [("a", 1.0)]

def test_dimension_guard():
    i = InMemoryVectorIndex(); i.add(Vector("a", (1.0, 0.0)))
    try: i.add(Vector("b", (1.0,)))
    except ValueError: pass
    else: raise AssertionError("dimension mismatch accepted")
