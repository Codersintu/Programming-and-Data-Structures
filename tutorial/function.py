# Recursion
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n* factorial(n-1)

num=factorial(8)
print(num)

# problem 1
def greates():
    a=int(input("enter number..."))
    b=int(input("enter number..."))
    c=int(input("enter number..."))
    if(a>b and a>c):
      return  print("a")
    elif (b>c and b>a):
       return print("b")
    else :return "c"

r=greates()
print(r)


# problem 2
def converter() :
   c=int(input("enter celcus ...."))
   return c*9/5

cb=converter()
print(cb)