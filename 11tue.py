#s={1,2,3,4}
#print(type(s))

#s={1,2,3,4,4,3,2,1}
#print(s)

#s=set()
#print(type(s))


#s={1,2}
#print(s[1])  # set does not relation with index

#to add the set
#s={1,2,3,4}
#s.add(6)
#print(s)

#s.update([8,9,7])
#print(s)

#s.update({1,23},[11,22])
#print(s)


#to delete the element t use discard
#s.discard(23)
#print(s)

#A={1,2,3,4,56,7,8,9}
#A.pop()
#print(A)


#set1={1,2,3}
#set2={4,3,6}
# print(set1|set2)
#print(set1.union(set2))
#print(set1&set2)
#print(set1-set2)
#print(set1.difference(set2))
#print(set1^set2)    


#x={"a","b","c","d"}
#y={"a","b","l"}
#print("set 'x' is sub set of'y'?",x.issubset(y))
#print("set 'y' is sub set of'x'?",y.issubset(x))


# lst=["hiia","byya","gooda"]
# S=set(lst)
# print(S)
# common_chars = set(lst[0])
# common_char=S.intersection(*lst)
# # print(common_char)
# # print(common_char & set(lst))
# for i in lst[1:]:
#     # common_char=common_char&set(lst)
#     common_char=common_char&S
# print(common_char)





# lst=["hiia","byya","gooda"]
# lst1=["surbhi","khushi","sneha"]
# print("-----------------------------------------------------------------------------------------")
# print(lst1)
# S=set(lst1)
# print(S)

# common_chars = set(lst1[0])


# for i in lst1[1:]:
#     common_chars = common_chars & set(i)  

# print("Common characters:", common_chars)


lst=["surbhi","khushi","suneha"]
common_chars = set(lst[0])

for i in lst[1]:
    common_chars=common_chars& set(i)
print(common_chars)    






