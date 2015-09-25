import collections
import time
from random import randint
t1=time.time()
class Document:
    title=''
    data=''
    listed=0
    keywords={}
    def __init__(self,t):
        self.title=t
        self.data=''
        self.listed=0
        for x in range(100):
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
for i in range(5000):
    exec("d%d=Document('d%d')"%(i,i))
    exec("documents.append(d%d)"%i)

'''
randnumbers=[]
for i in range(100):
    randnumbers.append(randint(0,1))
for i in range(5000):
    for j in range (100):
        exec("d%d.keywords[%d]=bool(randnumbers[%d])"%(i,j,j))
'''

#------------------------------------#



person=Person('John')
person.Qchange('k4')
person.Qchange('k2')

final1=set()
final2={}
for d in documents:
    final2[d]=0
for d in documents:
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k49'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k22'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k34'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k40'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k20'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k49'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k22'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k34'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k40'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k20'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k49'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k22'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k34'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k40'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k20'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k49'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k22'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k34'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k40'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k20'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k49'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k22'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k34'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k40'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k20'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k49'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k22'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k34'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k40'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k20'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k49'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k22'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k34'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k40'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k20'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k49'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k22'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k34'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k40'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k20'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k49'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k22'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k34'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k40'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k20'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k49'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k22'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k34'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k40'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k20'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k49'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k22'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k34'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k40'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k20'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k49'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k22'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k34'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k40'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k20'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k49'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k22'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k34'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k40'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k20'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k49'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k22'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k34'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k40'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k20'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k49'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k22'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k34'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k40'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k20'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k49'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k22'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k34'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k40'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k20'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k49'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k22'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k34'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k30'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k1'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k38'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k40'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k20'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k2'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k3'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k4'] and d.keywords[1]):
        final1.add((d,5))
    if (person.questionaire['k5'] and d.keywords[2]):
        final1.add((d,4))
    if (person.questionaire['k6'] and d.keywords[1]):
        final1.add((d,5))
'''final1.add((d998,90))
final1.add((d999,90))
final1.add((d997,80))
final1.add((d996,70))
final1.add((d995,60))
final1.add((d299,50))
final1.add((d199,30))
final1.add((d299,900))
final1.add((d399,904))
final1.add((d975,905))
final1.add((d976,906))
final1.add((d977,907))
final1.add((d978,905))
final1.add((d989,904))
final1.add((d979,903))
final1.add((d980,905))
final1.add((d982,907))
final1.add((d981,906))
final1.add((d983,905))
final1.add((d984,903))
final1.add((d985,902))
final1.add((d986,904))
final1.add((d987,905))
final1.add((d988,906))
final1.add((d989,907))
final1.add((d199,908))'''
for x in final1:
    final2[x[0]]+=x[1]
readable={}
for k in final2:
    readable[str(k)]=final2[k]
print(sorted(readable, key=readable.get, reverse=True)[:20])
t2=time.time()
print((t2-t1))

