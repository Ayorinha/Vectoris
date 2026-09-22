from vectoris.evaluation import RetrievalCase,evaluate

def test_evaluation_returns_mrr():
    assert evaluate([RetrievalCase("q",(0,1))])["mrr"] == .5
