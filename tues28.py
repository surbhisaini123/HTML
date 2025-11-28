# num=-9876
# print(abs(num))

# lst={1,2,3,4,}
# print(all(lst))


# print(divmod(9,2))

# A=range(-10,10)
# print(list(A))



# a=[1,2,3,4,5,6,7]
# def power(a):
#     return a **2
# q=list(map(power,a))
# print(q)



# producct =1

# lst=(1,2,3,4)
# for num in 


# a=int(input("enter first num========"))


def Addition(a,b):
   return a+b
def Subtraction(a,b):
     return a-b
 
def Multiplication(a,b):
    return a*b
def Division(a,b):
    return a/b



print("select option")
print("1.Addition")
print("2.Subtraction")
print("3.multiplication")
print("4.Division")


# choice=1,2,3,4
print()
choice=input(input("enter choice"))

a=float(input("enter first num"))
b=float(input("enter second num"))

if choice==1:
    print("Addition",a,b,Addition(a,b))
elif choice==2:   
    print("substraction",a,b,Subtraction(a,b))
elif choice==3:
    print("multipllication",a,b,Multiplication(a,b))    
elif choice==4:
    print("division",a,b,Division(a,b))    
else:
    print("invalid")  