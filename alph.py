# A, B, C=int,input().split()
# minimum=min(A,B,C)
# maximum=max(A,B,C)

# print(minimum,maximum)

# F1,S1=input().split()
# F2,S2=input().split()
# if S1==S2:
#     print("ARE BROTHER")
# else:
#     print("NOT")    


# CHAR= input()

# if CHAR>=65  and CHAR<=90:
#     print("it is capital")
# elif CHAR>=97 and CHAR<=122:
#     print("it is small")
# else:
#     print("digit") 

# X=input()
# if X.isdigit():
#     print("IS DIGIT")
# else:
#     print("ALPHA")
#     if X.isupper():
#         print("IS CAPITAL") 
#     else:
#         print("IS SMALL")       



# X=input()

# if X.isupper():
#     print(X.islower())
# else:
#     print(X.isupper)    


expr=input()
if '+'in expr:
    A,B=expr.split('+')
    print(int(A)+int(B))
elif '-' in expr:
        A,B=expr.split('-')
        print(int(A)-int(B))        
elif'*' in expr:
      A,B=expr.split('*')
      print(int(A)*int(B))
elif'/' in expr:
       A,B=expr.split('/')
       print(int(A)//int(B))
            

              
