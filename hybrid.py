import implementation
import collections
import time
from random import randint
import copy
import random
import bisect
import sys

#PRs:

def general_PRs(d,p):
    """Document->Person->int
    Generatized version of implementation.PRs
    """
    k=0
    if (p.questionaire['works_in_industry'] and d.keywords['industry']):
        k+=5
    if (p.questionaire['environmentalist'] and d.keywords['ocean']):
        k+=4
    if (p.questionaire['economist'] and d.keywords['economics']):
        k+=5
    if (p.questionaire['30orOlder'] and d.keywords['foradults']):
        k+=4
    if (p.questionaire['likesmath'] and d.keywords['math']):
        k+=5
    if (p.questionaire['hatesmath'] and d.keywords['math']):
        k-=7
    if (p.questionaire['SellsOil'] and d.keywords['excessoil']):
        k+=5
    if (p.questionaire['lovesanimals'] and d.keywords['animals']):
        k+=4
    if (p.questionaire['isDoctor'] and d.keywords['medical']):
        k+=5
    if (not p.questionaire['works_in_industry'] and d.keywords['industry']):
        k-=2
    if (not p.questionaire['environmentalist'] and d.keywords['ocean']):
        k-=2
    if (not p.questionaire['economist'] and d.keywords['economics']):
        k-=2
    if (not p.questionaire['30orOlder'] and d.keywords['foradults']):
        k-=1
    if (not p.questionaire['likesmath'] and d.keywords['math']):
        k-=2
    if (not p.questionaire['SellsOil'] and d.keywords['excessoil']):
        k-=1
    if (not p.questionaire['lovesanimals'] and d.keywords['animals']):
        k-=1
    if (not p.questionaire['isDoctor'] and d.keywords['medical']):
        k-=2
    return k

#Brute force
def general_brute_force(K,docs,p):
    D={}
    for d in docs:
        D[d.title]=general_PRs(d,p)

    return sorted(D, key=D.get, reverse=True)[:K]

def general_brute_force_iter(I,K,docs,p):
    return general_brute_force(K,docs,p)

#stochastic local search
def neighbors(d):
    neighbors=[]
    for x in d.keywords:
        k=copy.copy(d.keywords)
        k[x]=not k[x]
        d1=implementation.Document('n')
        d1.assign(k)
        neighbors.append(copy.copy(d1))
    return neighbors


def general_neighbors2(d,dke):
    neighbors=[]
    for x in d.keywords:
        k=copy.copy(d.keywords)
        k[x]=not k[x]
        d1=implementation.Document('n')
        d1.assign(k)
        if d1.keywords in dke:
            neighbors.append(copy.copy(d1))
    return neighbors

def gen_doc_key_combos(docs):
    """[Documents] -> [dict(str,Boolean)]
    Generate a list of document keyword combinations from a
    list of documents."""
    dk=[]
    for d in docs:
        dk.append(d.keywords)
    return dk


def general_FLS(I,K,docs,p):
    random.seed()
    d=random.choice(docs)
    top=[]
    k=general_PRs(d,p)
    for i in range(I):
        neighbors1=neighbors(d)
        r={}                        
        for x in neighbors1:
            r[x]=general_PRs(x,p)
        m=max(r, key=r.get)
        if r[m]>k:
            top.append(m)
            d=m
            k=r[m]
        else:
            d=random.choice(docs)
#    top=top.sort()
    top=top[len(top)-1:len(top)-1-K:-1]
    return top

def general_SLS(I,K,docs,p):
    random.seed()
    d=random.choice(docs)
    top=[]
    k=general_PRs(d,p)
    for i in range(I):
        r = { r:general_PRs(r,p) for r in neighbors(d) }
        r = { k1:v for k1, v in r.items() if v > k }
        if len(r)>0:
            d = random.choice(list(r.keys()))
            bisect.insort(top, d)
            k=r[d]
        else:
            d=random.choice(docs)
            bisect.insort(top, d)

    top=top[len(top)-1:len(top)-(K+1):-1]
    return top


def general_SLS2(I,K,docs,p):
    random.seed()
    dke = gen_doc_key_combos(docs)
    d=random.choice(docs)
    top=[]
    k=general_PRs(d,p)
    for i in range(I):
        r = { r:general_PRs(r,p) for r in general_neighbors2(d,dke) }
        r = { k1:v for k1, v in r.items() if v > k }
        if len(r)>0:
            d = random.choice(list(r.keys()))
            bisect.insort(top, d)
            k=r[d]
        else:
            d=random.choice(docs)
            bisect.insort(top, d)

    top=top[len(top)-1:len(top)-(K+1):-1]
    return top


def uniqueL(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]



def make_category_list():
    """None -> dict(str,Person)
    Make a list of persons, each representing a category.
    """
    plist={}
    pbase=implementation.Person('%imaginary%')
    for k in pbase.questionaire:
        plist[str(k)] = implementation.Person('%imaginary%'+str(k))
        plist[str(k)].Qchange(str(k))
    return plist

def use_category_list(clist,docs,method,I,K):
    """dict(str,Person) -> [Document] -> (int->int->Person->[Document]) ->
      int -> int -> dict(str,[Document])"""
    outdct = {}
    for k in clist:
        cat = clist[k]
        outdct[k] = method(I,K,docs,cat)
    return outdct
        
def use_category_list_brute(clist,docs,I,K):
    return use_category_list(clist,docs,general_brute_force_iter,I,K)
def use_category_list_FLS(clist,docs,I,K):
    return use_category_list(clist,docs,general_FLS,I,K)
def use_category_list_SLS(clist,docs,I,K):
    return use_category_list(clist,docs,general_SLS,I,K)
def use_category_list_SLS2(clist,docs,I,K):
    return use_category_list(clist,docs,general_SLS2,I,K)

def fancy_results(dres, file=sys.stdout):
    """dict(str,[Document]) -> None"""
    for x in dres:
        print(str(x)+": ",file=file)
        for y in dres[x]:
            print("\t"+str(y),file=file)
    return

