from vectoris.benchmark import recall_at_k,mrr
def test_metrics():
 r=["b","a","c"]; e=["a","c"]; assert recall_at_k(r,e,2)==.5; assert mrr(r,e)==.5
