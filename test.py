# 5 * 4 * 3 *2 * 1 = 5!
# def fact(num):
#     if num == 1:
#        return num
#     else:   
#         return num * fact(num-1)
    

# print(fact(5))


def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))

print(fib(6))
