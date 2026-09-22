def recall_at_k(results,expected,k): return 1.0 if not expected else len(set(results[:k])&set(expected))/len(expected)
def mrr(results,expected):
 for i,x in enumerate(results,1):
  if x in expected:return 1/i
 return 0.0
