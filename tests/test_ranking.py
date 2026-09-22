from vectoris.ranking import ndcg_at_k

def test_ndcg_is_bounded():
    value = ndcg_at_k(["a", "b"], {"a": 3.0, "b": 1.0}, 2)
    assert 0.0 <= value <= 1.0
