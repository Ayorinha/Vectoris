from vectoris.benchmark import *
def test_metrics(): assert recall_at_k(['b','a'],['a','c'],2)==.5 and mrr(['b','a'],['a'])==.5
