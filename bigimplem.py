import collections
import time
from random import randint
import random
import copy
import bisect

class Document:
    title=''
    data=''
    listed=0
    keywords={}
    def __init__(self,t):
        self.title=t
        self.data=''
        self.listed=0
        for x in range(25):
            self.keywords[x]=True
    def __str__(self):
        return self.title
    def add_keyword(self,word):
        self.keywords[word]=True
    def print_keywords(self):
        print(self.keywords)
    def remove_keyword(self,word):
        self.keywords[word]=False
    def increase(self,n):
        self.listed+=n
    def assign(self,kI):
        self.keywords=kI
    def __hash__(self):
        return hash(PRs(self))
    def __ne__(self, other):
        return PRs(self)!=PRs(other)
    def __lt__(self,other):
        return PRs(self)<PRs(other)
    def __le__(self,other):
        return PRs(self)<=PRs(other)
    def __gt__(self,other):
        return PRs(self)>PRs(other)
    def __ge__(self,other):
        return PRs(self)>=PRs(other)

class Person:
    name=''
    questionaire={}
    for i in range(50):
        exec("questionaire['k%d']=True"%i)
    def __init__(self,nam):
        self.name=nam
    def Qchange(self,q):
        self.questionaire[q]=not self.questionaire[q]    
    def print_q(self):
        print(self.questionaire)
        
#-------------------------------------#

documents=[]
for i in range(100000):
    exec("d%d=Document('d%d')"%(i,i))
    exec("d%d.title='d%d'"%(i,i))
    exec("documents.append(d%d)"%i)


#randnumbers=[]
#for i in range(100):
 #   randnumbers.append(randint(0,1))
for i in range(100000):
    exec("k%d={}"%i)
    for j in range(25):
        exec("k%d[%d]=bool(randint(0,1))"%(i,j))

for i in range(100000):
    exec("d%d.assign(k%d)"%(i,i))


#------------------------------------#


person=Person('John')
person.Qchange('k4')
person.Qchange('k2')


def PRs(d):
    k=0
    if (person.questionaire['k1'] and d.keywords[1]):
        k+=5
    if (person.questionaire['k38'] and d.keywords[2]):
        k+=4
    if (person.questionaire['k49'] and d.keywords[3]):
        k+=5
    if (person.questionaire['k30'] and d.keywords[4]):
        k+=4
    if (person.questionaire['k2'] and d.keywords[5]):
        k+=5
    if (person.questionaire['k3'] and d.keywords[6]):
        k+=4
    if (person.questionaire['k4'] and d.keywords[7]):
        k+=5
    if (person.questionaire['k5'] and d.keywords[8]):
        k+=4
    if (person.questionaire['k6'] and d.keywords[9]):
        k+=5
    if (person.questionaire['k1'] and d.keywords[10]):
        k+=5
    if (person.questionaire['k22'] and d.keywords[11]):
        k+=4
    if (person.questionaire['k34'] and d.keywords[12]):
        k+=5
    if (person.questionaire['k30'] and d.keywords[13]):
        k+=4
    if (person.questionaire['k2'] and d.keywords[14]):
        k+=5
    if (person.questionaire['k3'] and d.keywords[15]):
        k+=4
    if (person.questionaire['k4'] and d.keywords[16]):
        k+=5
    if (person.questionaire['k5'] and d.keywords[17]):
        k+=4
    if (person.questionaire['k6'] and d.keywords[18]):
        k+=5
    if (person.questionaire['k1'] and d.keywords[19]):
        k+=5
    if (person.questionaire['k38'] and d.keywords[20]):
        k+=4
    if (person.questionaire['k40'] and d.keywords[21]):
        k+=5
    if (person.questionaire['k20'] and d.keywords[22]):
        k+=4
    if (person.questionaire['k2'] and d.keywords[23]):
        k+=5
    if (person.questionaire['k3'] and d.keywords[24]):
        k+=4
    if (person.questionaire['k4'] and d.keywords[25]):
        k+=5
    if (person.questionaire['k5'] and d.keywords[24]):
        k+=4
    if (person.questionaire['k6'] and d.keywords[23]):
        k+=5
    if (person.questionaire['k1'] and d.keywords[22]):
        k+=5
    if (person.questionaire['k38'] and d.keywords[21]):
        k+=4
    if (person.questionaire['k49'] and d.keywords[20]):
        k+=5
    if (person.questionaire['k30'] and d.keywords[11]):
        k+=4
    if (person.questionaire['k2'] and d.keywords[12]):
        k+=5
    if (person.questionaire['k3'] and d.keywords[13]):
        k+=4
    if (person.questionaire['k4'] and d.keywords[14]):
        k+=5
    if (person.questionaire['k5'] and d.keywords[15]):
        k+=4
    if (person.questionaire['k6'] and d.keywords[16]):
        k+=5
    if (person.questionaire['k1'] and d.keywords[17]):
        k+=5
    if (person.questionaire['k22'] and d.keywords[18]):
        k+=4
    return k


#Brute force:
def brute_force(K):
    D={}
    for d in documents:
        D[d.title]=PRs(d)

    return sorted(D, key=D.get, reverse=True)[:K]
    

#SLS:
def neighbors(d):
    neighbors=[]
    for x in range(25):
        k=copy.copy(d.keywords)
        k[x]=not k[x]
        dR=Document('n')
        dR.assign(k)
        neighbors.append(copy.copy(dR))
    return neighbors

dk=[]
for d in documents:
    dk.append(d.keywords)

def neighbors2(d):
    neighbors=[]
    for x in d.keywords:
        k=copy.copy(d.keywords)
        k[x]=not k[x]
        d1=Document('n')
        d1.assign(k)
        if d1.keywords in dk:
            neighbors.append(copy.copy(d1))
    return neighbors

def neighbors3(d):
    neighbors=[]
    for i in range(5):
        neighbors.append(random.choice(documents))
    return neighbors


def FLS(I,K):
    random.seed()
    d=random.choice(documents)
    top=[]
    k=PRs(d)
    for i in range(I):
        r = { r:PRs(r) for r in neighbors3(d) }
        m=max(r, key=r.get)
        if r[m]>k:
            bisect.insort(top, m)
            d=m
            k=r[m]
        else:
            bisect.insort(top, d)
            d=random.choice(documents)
            k=PRs(d)
    top=uniqueL(top)
    top=top[len(top)-1:len(top)-1-K:-1]
    return top

def uniqueL(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]

def SLS(I,K):
    random.seed()
    d=random.choice(documents)
    top=[]
    k=PRs(d)
    for i in range(I):
        r = { r:PRs(r) for r in neighbors(d) }
        r = { k1:v for k1, v in r.items() if v > k }
        if len(r)>0:
            d = random.choice(list(r.keys()))
            bisect.insort(top, d)
            k=r[d]
        else:
            d=random.choice(documents)
            bisect.insort(top, d)
            k=PRs(d)

    top=top[len(top)-1:len(top)-(K+1):-1]
    return top

def SLS3(I,K):
    random.seed()
    d=random.choice(documents)
    top=[]
    k=PRs(d)
    for i in range(I):
        r = { r:PRs(r) for r in neighbors3(d) }
        r = { k1:v for k1, v in r.items() if v > k }
        if len(r)>0:
            d = random.choice(list(r.keys()))
            bisect.insort(top, d)
            k=r[d]
        else:
            d=random.choice(documents)
            bisect.insort(top, d)
            k=PRs(d)
#    top=[x for x in top if x.keywords in dk]
    top=top[len(top)-1:len(top)-(K+1):-1]
    return top

def SLS2(I,K):
    random.seed()
    d=random.choice(documents)
    top=[]
    k=PRs(d)
    for i in range(I):
        r = { r:PRs(r) for r in neighbors2(d) }
        r = { k1:v for k1, v in r.items() if v > k }
        if len(r)>0:
            d = random.choice(list(r.keys()))
            bisect.insort(top, d)
            k=r[d]
        else:
            bisect.insort(top, d)
            d=random.choice(documents)
            k=PRs(d)
 
    top=top[len(top)-1:len(top)-(K+1):-1]
    return top


t1=time.time()
brute_force(10)
t2=time.time()
print(t2-t1)

t1=time.time()
FLS(20,10)
t2=time.time()
print(t2-t1)

t1=time.time()
SLS3(20,10)
t2=time.time()
print(t2-t1)
