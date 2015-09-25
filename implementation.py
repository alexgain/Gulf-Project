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
        self.keywords={'industry':False,'economics':False,'ocean':False,'foradults':False,'medical':False,'math':False,'excessoil':False,'animals':False,\
                       'sugar':False}

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
    questionaire={'works_in_industry':False,'environmentalist':False,'economist':False,'30orOlder':False,\
                  'diabetic':False,'likesmath':False,'hatesmath':False,'SellsOil':False,'lovesanimals':False,'isDoctor':False}
    def __init__(self,nam):
        self.name=nam
    def Qchange(self,q):
        self.questionaire[q]=not self.questionaire[q]    
    def print_q(self):
        print(self.questionaire)    
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
final1=set()
final2={}
for d in documents:
    final2[d]=0

for d in documents:
    if (person.questionaire['works_in_industry'] and d.keywords['industry']):
        final1.add((d,5))
    if (person.questionaire['environmentalist'] and d.keywords['ocean']):
        final1.add((d,4))
    if (person.questionaire['economist'] and d.keywords['economics']):
        final1.add((d,5))
    if (person.questionaire['30orOlder'] and d.keywords['foradults']):
        final1.add((d,4))
    if (person.questionaire['likesmath'] and d.keywords['math']):
        final1.add((d,5))
    if (person.questionaire['hatesmath'] and d.keywords['math']):
        final1.add((d,-7))
    if (person.questionaire['SellsOil'] and d.keywords['excessoil']):
        final1.add((d,5))
    if (person.questionaire['lovesanimals'] and d.keywords['animals']):
        final1.add((d,4))
    if (person.questionaire['isDoctor'] and d.keywords['medical']):
        final1.add((d,5))
    if (not person.questionaire['works_in_industry'] and d.keywords['industry']):
        final1.add((d,-2))
    if (not person.questionaire['environmentalist'] and d.keywords['ocean']):
        final1.add((d,-2))
    if (not person.questionaire['economist'] and d.keywords['economics']):
        final1.add((d,-2))
    if (not person.questionaire['30orOlder'] and d.keywords['foradults']):
        final1.add((d,-1))
    if (not person.questionaire['likesmath'] and d.keywords['math']):
        final1.add((d,-2))
    if (not person.questionaire['SellsOil'] and d.keywords['excessoil']):
        final1.add((d,-1))
    if (not person.questionaire['lovesanimals'] and d.keywords['animals']):
        final1.add((d,-1))
    if (not person.questionaire['isDoctor'] and d.keywords['medical']):
        final1.add((d,-2))


for x in final1:
    final2[x[0]]+=x[1]
readable={}
for k in final2:
    readable[str(k)]=final2[k]
print(sorted(readable, key=readable.get, reverse=True)[:20])
t2=time.time()
print((t2-t1))











    
