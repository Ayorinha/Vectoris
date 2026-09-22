from vectoris.core import *

def test_vector():\n i=InMemoryVectorIndex();i.add(Vector("a",(1,0)));assert i.search((1,0))[0][0]=="a"
