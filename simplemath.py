# x=888
# def add(a,b):
#     print("sum=",a+b)
# def product(a,b):
#     print("product",a*b)    

# def triangle(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print("#  ",end='')
#         print()    



# n=1234



def palindome(n):
    
    start=0
    end=n-1
    for i in range(1,n):
        for j in range(n-1,1):
            if i==j:
                print("n is palindrome")
            else:
                print("nooooooooooooooooo")    

palindome(129765)