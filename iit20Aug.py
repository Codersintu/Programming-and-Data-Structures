# what is Recursion?
# recursion is a programming technique where a function calls itself to solve a problem
# by breaking it into smaller subproblems.

# why use recursion?
# (1)to solve complex problem that can be reduced to smaller,similar problems.
# (2)simplifies code for tree/graph,backtracking mathematical problems.

# def say_hello(n):
#     if n==0:
#         return n
#     print("Hello")
#     say_hello(n-1)

# print(say_hello(0))

# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
    
# print(factorial(5))

# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
    
# print(fibonacci(10))

def list_sum(num_list):
    if len(num_list)==0:
        return 0
    else:
        return num_list[0]+list_sum(num_list[1:])
print(list_sum([1,2,3,4,5]))

# reverse a string
def reverse_string(s):
    if len(s)==0:
        return s
    else:
        return reverse_string(s[1:])+s[0]
    
print(reverse_string("hello"))
