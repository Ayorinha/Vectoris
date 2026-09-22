from vectoris.metrics import reciprocal_rank,dcg

def test_reciprocal_rank_and_dcg():
    assert reciprocal_rank([0,1]) == .5
    assert dcg([1,0]) == 1.0
