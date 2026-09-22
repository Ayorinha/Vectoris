from vectoris.core import InMemoryVectorIndex, Vector

def test_vector():
    index = InMemoryVectorIndex()
    index.add(Vector("a", (1, 0)))
    assert index.search((1, 0))[0][0] == "a"
