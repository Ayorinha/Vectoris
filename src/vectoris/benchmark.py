from dataclasses import dataclass
@dataclass(frozen=True)
class Case: query:str; expected:list[str]
def recall_at_k(results:list[str], expected:list[str], k:int)->float:
 if not expected:return 1.0
 return len(set(results[:k])&set(expected))/len(expected)
def mrr(results:list[str], expected:list[str])->float:
 for i,x in enumerate(results,1):
  if x in expected:return 1/i
 return 0.0
