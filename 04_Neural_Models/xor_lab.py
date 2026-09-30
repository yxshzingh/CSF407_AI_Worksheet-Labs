import torch
from torch import nn
import torch.nn.functional as F
torch.set_num_threads(1)
X=torch.tensor([[0.,0.],[0.,1.],[1.,0.],[1.,1.]])
y=torch.tensor([[0.],[1.],[1.],[0.]])
classes=torch.tensor([0,1,1,2])
class BinaryNet(nn.Module):
    def __init__(self, activation):
        super().__init__(); self.fc1=nn.Linear(2,2); self.fc2=nn.Linear(2,1); self.activation=activation
    def forward(self,x): return self.fc2(self.activation(self.fc1(x)))
def train(act_name, seed=2, steps=1000):
    torch.manual_seed(seed); act={"sigmoid":torch.sigmoid,"tanh":torch.tanh,"relu":F.relu}[act_name]
    m=BinaryNet(act); opt=torch.optim.Adam(m.parameters(),lr=0.05); lossfn=nn.BCEWithLogitsLoss(); initial=None; early_grad=None
    for step in range(steps):
        opt.zero_grad(); loss=lossfn(m(X),y)
        if initial is None: initial=loss.item()
        loss.backward()
        if step==0: early_grad=m.fc1.weight.grad.detach().norm().item()
        opt.step()
    with torch.no_grad(): probs=torch.sigmoid(m(X)).squeeze().tolist(); pred=[int(p>=0.5) for p in probs]
    return m,initial,loss.item(),probs,pred,early_grad
def symmetry():
    torch.manual_seed(2); m=BinaryNet(torch.sigmoid)
    with torch.no_grad():
        for p in m.parameters(): p.zero_()
    opt=torch.optim.SGD(m.parameters(),lr=0.5); lossfn=nn.BCEWithLogitsLoss(); rows=[]
    for _ in range(5):
        opt.zero_grad(); loss=lossfn(m(X),y); loss.backward(); opt.step(); rows.append(m.fc1.weight.detach().clone())
    return rows
def multiclass():
    torch.manual_seed(2); m=nn.Sequential(nn.Linear(2,2),nn.Tanh(),nn.Linear(2,3)); opt=torch.optim.Adam(m.parameters(),lr=0.05)
    for _ in range(1000):
        opt.zero_grad(); loss=F.cross_entropy(m(X),classes); loss.backward(); opt.step()
    with torch.no_grad(): probs=F.softmax(m(X),dim=1); pred=probs.argmax(1)
    return m,probs,pred,loss.item()
def main():
    print("Binary XOR experiments")
    for a in ["sigmoid","tanh","relu"]:
        _,ini,fin,probs,pred,g=train(a); print(a,"initial=",round(ini,6),"final=",round(fin,6),"correct=",pred==[0,1,1,0],"grad_norm_step0=",round(g,6),"probs=",[round(v,6) for v in probs])
    rows=symmetry(); print("Symmetry zero-init rows identical:",all(torch.allclose(r[0],r[1]) for r in rows))
    _,probs,pred,loss=multiclass(); print("Three-class final loss=",round(loss,6),"pred=",pred.tolist()); print("Probabilities="); print(probs.detach().numpy()); print("First row sum=",probs[0].sum().item())
if __name__=="__main__": main()
