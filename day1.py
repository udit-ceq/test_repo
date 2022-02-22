# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 15:35:03 2021

@author: 91798
"""
############# Python Day 1 ##############################
'''
Python is an interpreted, object-oriented, high-level programming language with 
dynamic semantics. Its high-level built in data structures, combined with dynamic typing
 and dynamic binding, make it very attractive for Rapid Application Development.
 
 
lateest version - Python 3 
 
-> compatibility with Machine Learning , Iot, AWS

About today's class :
    Syntax
    print("hghgh:{:.2f} and {}".format(var1,var2))
    How to run , IDEs
    input()
    built in data structures- List, tuple, set, dict, string
    if-else clause 
    loops
    function creation 
    
    
    functions 
    names 
    modules
    class 
    
'''

List - Mutable, ordered, allow duplicacy:
    list creation 
    random access 
    append
    insert 
    pop
    remove
    deflist.clear(),reverse(),sort()
    slicing operations
    shallow copy and deep copy 
    List Comprehension
    
Tuples - ordered, immutable, allow duplicacy:
    tuple creation 
    tuple.index("abc")
    typecast
    import sys
    print(sys.getsizeof(my_list),'bytes')
import timeit
print(timeit.timeit(stmt="[0,1,2,3]",number=100000))

Dict - key,value pair, unordered , mutable:
    del dict["key"]
    dict.pop("key")
    dict.popitem() # last item
    for loop in dict:
    dict1.update(dict2)
    
set - unordered, mutable, no duplicacy
myset= {1,2,3,4}
myset=set()
set.add(13)
set.remove(13)
myset.clear()
myset.pop()
odds={1,3,5,7}
evens={2,4,6,8}
primes={1,3,5,7,11}
U=odds.unions(evens)
i=odds.intersects(evens)
odds.difference(evens)
odds.symmetricdifference(evens)
b={1,2,3,4}
a=frozenset(b)


string - ordered, immutable, text representation 
s="hello world"
s1="""djhdjhfjdfj
bjjd
"""
print(s1)
slicing
concattination = s1+s2
s.strip() # remove unnecessary spaces 
.uuper(),lower(),startswith(""),endswith(""), s1.find(""), s1.count(""),s1.replace("","")
list= s1.split() # default by space
mystr="".join(list) 



lambda expressions ::
    
json:
import json 
person={"Pid":"7218728","Name":"hhsudhu","age":"27","Address":"ddhsdhwbd wehdewkj"}

person_json=json.dumps(person,indent=4,sort_keys=True)
print(person_json)

with open("person.json",'w') as file:
    json.dump(person, file, indent=4)
    
    json.loads(personjson)# load into str
    
  
    
Python pickle module is used for serializing and de-serializing python object structures. 
The process to converts any kind of python objects (list, dict, etc.) into byte streams (0s and 1s) 
is called pickling or serialization or flattening or marshalling. 
We can converts the byte stream (generated through pickling) back into python objects by a process called as unpickling.

Why Pickle?:they allow us to easily transfer data from one server/system to another and then store it in a file or database.


import pickle
mylist = ['a', 'b', 'c', 'd']
with open('datafile.txt', 'wb') as fh:
   pickle.dump(mylist, fh)   
   
import pickle
pickle_off = open ("datafile.txt", "rb")
emp = pickle.load(pickle_off)
print(emp)



    
