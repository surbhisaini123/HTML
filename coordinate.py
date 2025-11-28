# int =input()
# int =input()

# string=input()

# float=input()

# print(int,int,string,float)




# a,b,c,d,e=input().split()
# a=int(a)
# b=int(b)
# c=str(c)
# d=float(d)
# e=float(e)
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)


# X=int(input())
# Y=int(input())

# # print(A)
# # print(B)
# print(X,"+",Y,"=" ,X+Y)
# print(X,"-",Y,"=" ,X-Y)
# print(X,"*",Y,"=" ,X*Y)



# A=int(X[0])
# for i in range(0):
#     if X[i]%2==0:
#         print("EVEN")
#     else:
#         print("ODD")   
# X=int(input()) 
# A=X//1000
# if A %2==0:
#     print("EVEN")
# else:
#     print("ODD")    

X=int(input())
Y=int(input())
if X==0 and Y==0:
    print("Origem")
elif X==0:
    print("Eixo X")    
elif Y==0:
    print("Eixo Y")    
elif X>0 and Y>0:
    print("Q1")    
elif X<0 and Y>0 :
    print("Q2")
elif X<0 and Y<0:
    print("Q3")
else:
    print("0Q4")    