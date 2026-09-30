
from collections import Counter, defaultdict
import random

DATA = [
"the cat sat on the mat","the cat sat on the rug","the dog sat on the mat",
"the dog ran to the park","the cat ran to the park","the dog sat on the rug"]
START, END = "<START>", "<END>"

def train(sentences):
    counts=defaultdict(Counter)
    for s in sentences:
        t=[START,START]+s.lower().split()+[END]
        for a,b,c in zip(t,t[1:],t[2:]): counts[(a,b)][c]+=1
    probs={}
    for ctx,c in counts.items():
        total=sum(c.values())
        probs[ctx]={x:n/total for x,n in sorted(c.items())}
    return counts,probs

def greedy(probs,ctx):
    d=probs.get(tuple(ctx),{})
    return max(d,key=d.get) if d else None

def sample(probs,ctx,rng):
    d=probs.get(tuple(ctx),{})
    if not d: return None
    return rng.choices(list(d),weights=list(d.values()),k=1)[0]

def generate(probs,rng=None,max_len=30):
    ctx=(START,START); out=[]
    for _ in range(max_len):
        nxt=sample(probs,ctx,rng) if rng else greedy(probs,ctx)
        if nxt is None or nxt==END: break
        out.append(nxt); ctx=(ctx[1],nxt)
    return " ".join(out)

if __name__=="__main__":
    counts,probs=train(DATA)
    print("SECOND-ORDER CPT")
    for c in sorted(probs): print(c,probs[c])
    print("\nNORMALISATION")
    for c,d in sorted(probs.items()): print(c,sum(d.values()))
    print("\nGREEDY")
    for i in range(5): print(i+1,generate(probs))
    print("\nSAMPLING seed=42")
    r=random.Random(42)
    for i in range(20): print(i+1,generate(probs,r))
