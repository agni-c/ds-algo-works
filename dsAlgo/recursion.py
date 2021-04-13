# factorial
#  5 * 4 * 3 *2 * 1 = 5!
# def fact(num):
#     if num == 1:
#        return num
#     else:   
#         return num * fact(num-1)
# print(fact(5))

# fibbonachi
# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return (fib(n-1) + fib(n-2))
# print(fib(6))

# power
# def power(n,p):
#     if p == 0:
#         return 1
#     else:
#         return  power(n,p-1) * n
# print(power(2,3))

# combnations
def fact(n):
    res = 1
    for i in range(2,n+1):
        res*=i
    return res
def combo(n,r):
    if n == 0:
        return 1
    else:
        return (fact(n)/(fact(r)*fact(n-r)))
print(combo(6,3))