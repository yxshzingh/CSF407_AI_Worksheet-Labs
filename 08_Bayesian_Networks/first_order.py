
from collections import Counter, defaultdict
import random

DATA = [
"the cat sat on the mat","the cat sat on the rug","the dog sat on the mat",
"the dog ran to the park","the cat ran to the park","the dog sat on the rug"]
START, END = "<START>", "<END>"

def train(sentences):
    counts=defaultdict(Counter)
    for s in sentences:
        t=[START]+s.lower().split()+[END]
        for a,b in zip(t,t[1:]): counts[a][b]+=1
    probs={}
    for a,c in counts.items():
        total=sum(c.values())
        probs[a]={b:n/total for b,n in sorted(c.items())}
    return counts,probs

def greedy(probs, current):
    d=probs.get(current,{})
    return max(d,key=d.get) if d else None

def sample(probs,current,rng):
    d=probs.get(current,{})
    if not d: return None
    return rng.choices(list(d),weights=list(d.values()),k=1)[0]

def generate(probs,rng=None,max_len=30):
    cur=START; out=[]
    for _ in range(max_len):
        nxt=sample(probs,cur,rng) if rng else greedy(probs,cur)
        if nxt is None or nxt==END: break
        out.append(nxt); cur=nxt
    return " ".join(out)

if __name__=="__main__":
    counts,probs=train(DATA)
    print("FIRST-ORDER CPT")
    for w in sorted(probs): print(w, probs[w])
    print("\nNORMALISATION")
    for w,d in sorted(probs.items()): print(w, sum(d.values()))
    print("\nPREDICTIONS")
    for w in ["<START>","the","cat","dog","sat","ran","on","to"]:
        print(w,"->",greedy(probs,w))
    print("\nGREEDY")
    for i in range(5): print(i+1,generate(probs))
    print("\nSAMPLING seed=42")
    r=random.Random(42)
    for i in range(20): print(i+1,generate(probs,r))
