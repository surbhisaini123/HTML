# lst=[2,3,2,4,3,5,5]

# seen=[]
# out=[]
# for i in lst :
#     if i not in seen:
#         seen.append(i)
#         out.append(i)
# print(out)  
# print(seen)  




# a=[1,3,9,5]
# target=8
# sum=[]
# for i in a:
#     for j in a:
#         A=i+j
#         if A ==target:
#             # print(a)
#             sum.append(i)
#             # sum.append(a[A])
# print(sum)


# A=[1,2,3,6,8,9]
# target=17
# sum=[]
# for i in range(len(A)):
#     for j in range(i+1,len(A)):
#         if A[i]+A[j]==target:
#             sum=[i,j]
#             break
# print(sum)        


A=[2,3,4,6,7]

Q=[]
s=[]

for i in A:
    for j in range(i+1,len(A)):
        Q=i+j
        # Q+j=s
        # s=Q+(j+1)
        # s=Q+(j+i)
        s=Q+(j+1)
  
print(s)    