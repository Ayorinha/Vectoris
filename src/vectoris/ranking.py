def ndcg_at_k(results, relevance, k):
    if k < 1: raise ValueError("k must be positive")
    gains=[relevance.get(x,0.0) for x in results[:k]]
    dcg=sum(g / __import__("math").log2(i+2) for i,g in enumerate(gains))
    ideal=sorted(relevance.values(), reverse=True)[:k]
    idcg=sum(g / __import__("math").log2(i+2) for i,g in enumerate(ideal))
    return dcg/idcg if idcg else 0.0
