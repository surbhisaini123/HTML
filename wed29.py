# def factorial(a):
#     fact=1
#     for i in range(a):
#         # F=a*fact*(a-1)
#         F=fact*(i-1)
#         return F
# W=factorial(5) 
# print(W)



# def Fibbonaseries(a):
#     b=0;c=1
#     nexterm=b+c
    
#     for i in range(a):
#         # print(b,c)
#     # while nexterm<=a:

      
#         # b=c
#         # c=nexterm
#         # nexterm=b+c
#         # return nexterm
#         if a<=i:
#             return a
#         else:
#             # fibonacci(a-1)+fibonacci(a-2)
           

    
      
# # Q=Fibbonaseries(10)  

# # print(Q)



def sum_natural_no(a):
    for i in range(a):
        if a<1:
            return 0
        else:
           return (a*(a-1))//2
    # print(A)       
 
A=sum_natural_no(5)

print()