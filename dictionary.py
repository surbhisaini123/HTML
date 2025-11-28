my_dict={}
#  dictionary with inteer key

A={1:'xxyz',2:'ab'}
print(A)

#dicctionary with mixed keys

A={'name':"Ssss",1:['qqq','pppp']}
print(A)


#create empty dictionary using dict()

A=dict()

A=dict(((1,'abc'),(2,'xyz')))  #create a dict with kist tuple
print(A)

S={'name':'satish','age':'19','Address':'delhi'}
print("age====",S['age'])
print(S['name'])
# print(S['hyy'])   error 

print(S.get('Address'))
print(S.get('Addr'))

#change in dictionary
A={'name':'XYZ','age':14,'Address':"bhu"}
A['name']='abc'
print(A)

#add new key 
A['deggre']='m.tech'
print(A)

#.pop use to delete the the element

M={'name':'asd','age':12,'addres':'qwe'}
print(M.pop('name'))
print(M)

#.popitem to use remove the element at the end

D={'name':'vgh','age':88,'ADD':'ddfd'}

D.popitem()
print(D)
#use del particular key
Q={1:2,3:2,4:6}
del Q[3]
print(Q)
#all clear item
Q={1:2,3:2,4:6}
Q.clear()
print(Q)

#puri dictnory delete
# Q={1:2,3:2,4:6}
# del Q
# print(Q)

#.copy se ek dictinary se dusri m copy karna

Q={1:2,3:2,4:6}
a=Q.copy()
print(a)

sub={}.fromkeys({'maths','english','hindi'},0)
print(sub)

Q={1:2,3:2,4:6}
print(Q.items())

Q={1:2,3:2,4:6}
print(Q.keys())
print(Q.values())

a={}
print(dir(a))
#loop
E={'b':1,'a':2,'d':3}
for i in E.items():
    print(i)

E={'b':1,'a':2,'d':3}
NEW={k:v for k,v in E.items() if v>2}
print(NEW)    

print("-------------------------------------------------------------------------")

E={'b':1,'a':2,'d':3}
NEW={k+'d':v*2 for k,v in E.items() if v>2}
print(NEW)    