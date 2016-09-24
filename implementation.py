import collections
import time
from random import randint
import copy
import random
import bisect


def keywords_hash(dk):
    out = 0
    sign = 1
    inc = 1
    for k in dk:
        out += sign*inc*(hash(k)+hash(dk[k]))
        sign = -sign
        inc += 1
    return out

class Document:
    title=''
    data=''
    listed=0
    keywords={}
    def __init__(self,t):
        self.title=t
        self.data=''
        self.listed=0
        self.keywords={'industry':False,'economics':False,'ocean':False,'foradults':False,'medical':False,'math':False,'excessoil':False,'animals':False,\
                       'sugar':False}

    def __str__(self):
        return self.title
    def __repr__(self):
        s = ""
        c = getattr(self,'__class__',None)
        if c is not None:
            m = getattr(self,'__module__',None)
            if m is not None:
                s += str(m)+'.'
            m = getattr(self,'__name__','Document')
            s += str(m)
        else:
            s = "Document"
        s += '('+repr(self.title)+')'
        return s
    def add_keyword(self,word):
        self.keywords[word]=True
    def print_keywords(self):
        print(self.keywords)
    def remove_keyword(self,word):
        self.keywords[word]=False
    def increase(self,n):
        self.listed+=n
    def assign(self,k):
        self.keywords=k

    #def __eq__(self, other):
#        return PRs(self) == PRs(other)
    def __hash__(self):
        #return hash(PRs(self))
        return keywords_hash(self.keywords)
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
    def __init__(self,nam):
        self.name=nam
        self.questionaire={'works_in_industry':False,'environmentalist':False,'economist':False,'30orOlder':False,\
                  'diabetic':False,'likesmath':False,'hatesmath':False,'SellsOil':False,'lovesanimals':False,'isDoctor':False}
        self.weights={'works_in_industry':0.0,'environmentalist':0.0,'economist':0.0,'30orOlder':0.0,\
                  'diabetic':0.0,'likesmath':0.0,'hatesmath':0.0,'SellsOil':0.0,'lovesanimals':0.0,'isDoctor':0.0}
    def Qchange(self,q):
        self.questionaire[q]=not self.questionaire[q]
    def print_q(self):
        print(self.questionaire)
    # cat is a str, w is a floating point num
    def set_weight(self,cat,w):
        self.weights[cat]=w

        
d1=Document('d1')
d2=Document('d2')
d3=Document('d3')
d4=Document('d4')
d5=Document('d5')
d6=Document('d6')
d7=Document('d7')
d8=Document('d8')
d9=Document('d9')
d10=Document('d10')
d11=Document('d11')
d12=Document('d12')
d13=Document('d13')
d14=Document('d14')
d15=Document('d15')
d16=Document('d16')
d17=Document('d17')
d18=Document('d18')
d19=Document('d19')
d20=Document('d20')
d21=Document('d21')
d22=Document('d22')
d23=Document('d23')
d24=Document('d24')
d25=Document('d25')
d26=Document('d26')
d27=Document('d27')
d28=Document('d28')
d29=Document('d29')
d30=Document('d30')

d1.add_keyword('industry')
d3.add_keyword('economics')
d5.add_keyword('medical')
d6.add_keyword('math')
d7.add_keyword('excessoil')
d8.add_keyword('animals')
d9.add_keyword('sugar')
d10.add_keyword('industry')
d12.add_keyword('ocean')
d13.add_keyword('economics')
d14.add_keyword('foradults')
d15.add_keyword('medical')
d16.add_keyword('math')
d17.add_keyword('excessoil')
d18.add_keyword('animals')
d19.add_keyword('sugar')
d21.add_keyword('industry')
d22.add_keyword('ocean')
d23.add_keyword('economics')
d24.add_keyword('foradults')
d25.add_keyword('medical')
d26.add_keyword('math')
d27.add_keyword('excessoil')
d28.add_keyword('animals')
d29.add_keyword('sugar')
d30.add_keyword('sugar')
d2.add_keyword('ocean')
d2.add_keyword('industry')
d2.add_keyword('math')
d2.add_keyword('animals')
d3.add_keyword('ocean')
d3.add_keyword('industry')
d3.add_keyword('math')
d4.add_keyword('industry')
d4.add_keyword('math')
d5.add_keyword('ocean')
d5.add_keyword('industry')
d5.add_keyword('math')
d5.add_keyword('animals')



documents=[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24,d25,d26,d27,d28,d29,d30]

person=Person('John')
person.Qchange('works_in_industry')
person.Qchange('environmentalist')
person.Qchange('likesmath')
person.Qchange('lovesanimals')


#PRs:

def PRs(d):
    k=0
    if (person.questionaire['works_in_industry'] and d.keywords['industry']):
        k+=5
    if (person.questionaire['environmentalist'] and d.keywords['ocean']):
        k+=4
    if (person.questionaire['economist'] and d.keywords['economics']):
        k+=5
    if (person.questionaire['30orOlder'] and d.keywords['foradults']):
        k+=4
    if (person.questionaire['likesmath'] and d.keywords['math']):
        k+=5
    if (person.questionaire['hatesmath'] and d.keywords['math']):
        k-=7
    if (person.questionaire['SellsOil'] and d.keywords['excessoil']):
        k+=5
    if (person.questionaire['lovesanimals'] and d.keywords['animals']):
        k+=4
    if (person.questionaire['isDoctor'] and d.keywords['medical']):
        k+=5
    if (not person.questionaire['works_in_industry'] and d.keywords['industry']):
        k-=2
    if (not person.questionaire['environmentalist'] and d.keywords['ocean']):
        k-=2
    if (not person.questionaire['economist'] and d.keywords['economics']):
        k-=2
    if (not person.questionaire['30orOlder'] and d.keywords['foradults']):
        k-=1
    if (not person.questionaire['likesmath'] and d.keywords['math']):
        k-=2
    if (not person.questionaire['SellsOil'] and d.keywords['excessoil']):
        k-=1
    if (not person.questionaire['lovesanimals'] and d.keywords['animals']):
        k-=1
    if (not person.questionaire['isDoctor'] and d.keywords['medical']):
        k-=2
    return k

#Brute force
def brute_force(K):
    D={}
    for d in documents:
        D[d.title]=PRs(d)

    return sorted(D, key=D.get, reverse=True)[:K]

#stochastic local search
def neighbors(d):
    neighbors=[]
    for x in d.keywords:
        k=copy.copy(d.keywords)
        k[x]=not k[x]
        d1=Document('n')
        d1.assign(k)
        neighbors.append(copy.copy(d1))
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


def FLS(I,K):
    random.seed()
    d=random.choice(documents)
    top=[]
    k=PRs(d)
    for i in range(I):
        neighbors1=neighbors(d)
        r={}                        
        for x in neighbors1:
            r[x]=PRs(x)
        m=max(r, key=r.get)
        if r[m]>k:
            top.append(m)
            d=m
            k=r[m]
        else:
            d=random.choice(documents)
#    top=top.sort()
    top=top[len(top)-1:len(top)-1-K:-1]
    return top

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
            d=random.choice(documents)
            bisect.insort(top, d)

    top=top[len(top)-1:len(top)-(K+1):-1]
    return top


def uniqueL(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]












    
