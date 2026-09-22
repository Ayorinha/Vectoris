from dataclasses import dataclass
import math
@dataclass(frozen=True)
class Vector:id:str;values:tuple[float,...]
class InMemoryVectorIndex:
 def __init__(self):self.items=[]
 def add(self,v):
  if not v.values:raise ValueError("empty vector")
  if self.items and len(v.values)!=len(self.items[0].values):raise ValueError("dimension mismatch")
  self.items.append(v)
 def search(self,q,k=5):
  if not self.items:return []
  if len(q)!=len(self.items[0].values):raise ValueError("dimension mismatch")
  def cos(v):
   n=math.sqrt(sum(x*x for x in q))*math.sqrt(sum(x*x for x in v));return sum(a*b for a,b in zip(q,v))/n if n else 0.0
  return [(v.id,cos(v.values)) for v in sorted(self.items,key=lambda x:cos(x.values),reverse=True)[:k]]
