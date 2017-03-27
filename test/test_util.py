
import sys
sys.path.append('/Users/qinmengyao/PythonProjects/python3/git_bodog/')
from main.util import Util as U

dictCmp = {}
for i in range(2,9):
    dictCmp[i] = i
print(dictCmp)

l = []
l.append(['Ac','Kc'])
l.append(['Ac','Kh'])
l.append(['Ac','As'])
l.append(['8c','8s'])
l.append(['Tc','Ts'])
l.append(['Qc','Qs'])
l.append(['5c','6s'])
l.append(['5s','6s'])
l.append(['3s','As'])
l.append(['2s','As'])
l.append(['9s','Ks'])
l.append(['Ts','Kh'])

for i in l:
    print(U.classifyHand(i))
