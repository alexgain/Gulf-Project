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


'''
asks person, "Which categories do you belong too?"
outputs a dictionary, with keys of Strings (identifier of person) and values of Person object
(imaginary person that represents only one category)
'''
def make_category_list():
    """None -> dict(str,Person)
    Make a list of persons, each representing a category.
    """
    pdict={}
    # class implementation, class Person
    # creating random Person object
    pbase=implementation.Person('%imaginary%')
    for k in pbase.questionaire:
        pdict[str(k)] = implementation.Person('%imaginary%'+str(k))
        pdict[str(k)].Qchange(str(k))
    return pdict

'''
returns a dictionary where the key is a string (name of category that
the list represents) and the value is a list of documents

clist -- list of people (that represent categories)
docs -- list of documents
method -- determines method to call e.g. FLS, SLS, etc.
I -- # of iterations for FLS, SLS, etc.
K -- # of docs
'''

def use_category_list(clist,docs,method,I,K):
    """dict(str,Person) -> [Document] -> (int->int->[Documents]->Person->[Document]) ->
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


'''
zips up the "top k" documents for each category, which may repeat documents in a list of
at most (# of categories)*(k) documents

input: dictionary -- key: string that is the category, value: list of documents in order that
best relate to that category

output: a list of documents
'''
# input: list l of ordered documents (repeats)
# output: final of list of documents (no repeats) of size k

def final_list(l, k):

    count = {}
    final = []
    
    # adds docs in order from input list ignoring repeats until length k
    for doc in l:
        if len(final) == k:
            break
        
        d = doc.title
        if d in count.keys():
            count[d] += 1
        else:
            count[d] = 1
            final.append(doc)

    return final

'''
def print_list(L):
    for i in L:
        print i, " "


class Document:
    title=''
    def __init__(self,t):
        self.title=t
    def __str__(self):
        return self.title

d1 = Document('d1')
d2 = Document('d2')
d3 = Document('d3')
d4 = Document('d4')
d5 = Document('d5')
d6 = Document('d6')
d7 = Document('d7')
d8 = Document('d8')
d9 = Document('d9')
d10 = Document('d10')

print_list(final_list([d1,d2,d3,d3,d4,d3,d5,d1,d10],10))
'''

