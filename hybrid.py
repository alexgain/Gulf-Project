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
    Generalized version of implementation.PRs
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

    return [find_doc_in_list(docs,a)
            for a in sorted(D, key=D.get, reverse=True)[:K]]

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
    """[Documents] -> [dict(str,bool)]
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
            if d not in top:
                bisect.insort(top, d)
            k=r[d]
        else:
            d=random.choice(docs)
            if d not in top:
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
            dx = find_doc_in_list_by_keywords(docs,d.keywords)
            if dx is not None:
                if dx not in top:
                    bisect.insort(top, dx)
                k=r[d]
        else:
            d=random.choice(docs)
            dx = find_doc_in_list_by_keywords(docs,d.keywords)
            if dx is not None:
                if dx not in top:
                    bisect.insort(top, dx)

    if len(top) >= K:
        pass
    else:
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
        pdict[str(k)].set_weight(str(k),1.0)
    return pdict


# input: dictionary created by make_category_list()
# output: list of categories (instances of class Person)
def cat_dict_to_cat_list(cat_dict):
    cat_list = []
    for i,j in cat_dict.items():
        cat_list.append(j)
    return cat_list



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



###############################################
# sample users Laura and Chris

lo = implementation.Person("Laura")
lo.Qchange('environmentalist')
lo.Qchange('economist')
lo.Qchange('lovesanimals')
lo.set_weight('environmentalist', 0.2)
lo.set_weight('economist', 0.3)
lo.set_weight('lovesanimals', 0.5)
#print (lo.name, lo.questionaire, lo.weights)

chris = implementation.Person("Chris")
chris.Qchange('30orOlder')
chris.Qchange('SellsOil')
chris.Qchange('works_in_industry')
chris.Qchange('lovesanimals')
chris.set_weight('30orOlder', 0.25)
chris.set_weight('SellsOil', 0.3)
chris.set_weight('works_in_industry', 0.35)
chris.set_weight('lovesanimals', 0.1)
#print (chris.name, chris.questionaire, chris.weights)

################################################
# create test documents

# very very applicable to lo
d1 = implementation.Document('d1')
d1.add_keyword('economics')
d1.add_keyword('animals')
d1.add_keyword('ocean')

# very very applicable to chris
d2 = implementation.Document('d2')
d2.add_keyword('foradults')
d2.add_keyword('excessoil')
d2.add_keyword('industry')

# semi-applicable to both chris and lo
d3 = implementation.Document('d3')
d3.add_keyword('ocean')
d3.add_keyword('animals')

# more applicable to chris than lo
d4 = implementation.Document('d4')
d4.add_keyword('medical')
d4.add_keyword('math')
d4.add_keyword('foradults')
d4.add_keyword('excessoil')
d4.add_keyword('industry')
d4.add_keyword('animals')

docs = [d1,d2,d3,d4]


# helper function
# takes string and creates an instance of class Person (category)
# returns the instance of class Person (category)
def str_to_cat(s):
    cat = implementation.Person("%s" % s)
    cat.Qchange(s)
    return cat

# generates clist for a user (helper method for list_per_user)
# clist is a list with each element as a category (str) the user is
def clist_per_user(person):
    clist = []
    for key,val in person.questionaire.items():
        if (val == True):
            clist.append(key)
        else:
            continue
    return clist

# helper function
def find_doc_in_list(docs, title):
    for d in docs:
        if d.title == title:
            return d
        else:
            continue
    return None #"Error. Document not found with that title."
def find_doc_in_list_by_title(docs, title):
    return find_doc_in_list(docs,title)
def find_doc_in_list_by_keywords(docs, keywords):
    for d in docs:
        if d.keywords == keywords:
            return d
        else:
            continue
    return None #"Error. Document not found with that title."
    

# Input:
# person is a user (instance of class Person)
# docs is a list of all documents in the system
# I is the number of iterations (moot point for brute force)
# K is the number of documents in final list
# Output:
# list of top k weighted documents for the specific user
def list_per_user(person, docs, I, K, typ="sls2"):

    # clist is a list of the categories the user belongs to
    clist = clist_per_user(person)

    cat_list = {}
    # convert list of strings to list of categories for person
    # cat_list is now a list of categories as instances of the class Person for the specific user
    for i in clist:
        cat_list[i] = str_to_cat(i)
        

    # final_dict is a dictionary with keys as categories and values as a list of docs for that category
    if typ=="brute":
        final_dict = use_category_list_brute(cat_list, docs, I, K)
    else:
        final_dict = use_category_list_SLS2(cat_list, docs, I, K)

    # for each document in value lists, store in dictionary as key and accumulate the value as weight
    weighted_docs = {}
    for cat_string,value_list in final_dict.items():
        
        # store weight and doc in dictionary weighted_docs
        cat_instance = str_to_cat(cat_string)
        for d in value_list:

            curr_doc = d #find_doc_in_list(docs, d)
            if curr_doc is not None:
                curr_weight = general_PRs(curr_doc, cat_instance)
                
                if d not in weighted_docs.keys():
                    weighted_docs[d] = curr_weight
                else:
                    weighted_docs[d] += curr_weight

    return select_top_k_docs(weighted_docs,K)

# helper function
# sorts dictionary of documents by weight (selects highest k docs)
# returns list of k docs (those most applicable to hybrid user)
def select_top_k_docs(dict_of_docs, k):
    final_list = sorted(dict_of_docs,key=dict_of_docs.get,reverse=True)[:k]
    return final_list


################################################
# FINAL TEST: do the methods return an accurate list of most applicable documents
# for hybrid users???

def post_evaluation(docs, person):
    n = 0
    for i in docs:
        n += general_PRs(i, person)
    return n

test_l = list_per_user(lo   , docs, 400, 3)
print(lo.name, "..", test_l, post_evaluation(test_l, lo))
test_l = list_per_user(lo   , docs, 400, 3, "brute")
print(lo.name, "[]", test_l, post_evaluation(test_l, lo))

test_l = list_per_user(chris, docs, 400, 3)
print(chris.name, "..", test_l, post_evaluation(test_l, chris))
test_l = list_per_user(chris, docs, 400, 3, "brute")
print(chris.name, "[]", test_l, post_evaluation(test_l, chris))
