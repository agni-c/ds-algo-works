# 1. parinting hello world
# --------------------------
# print("hello world")



# 1.1. Format string 


# 1.2 Indentation 

# Your indentation should be uniform else it will throw an error

# 2. take input
#  Python program showing  
# a use of input() 
# --------------------------
# val = input("Enter your value: ") 
# print(val)

# 3. Loops (For, while)
# ----------------------


# 4. If else (Conditionals)
# ----------------------

# 5. Functions 
# 6. List
# 7. Tuples 
# 8. Sets 
# 9. Lambda 
# 10. Map
#  11. Class
# 12. optional :  Inharitence
# 13. agar zinda rahe to do ek question






# Example Fizz Buzz function

def FizzBuzzFn(limit,firstNo,secondNo):
    for i in range(int(limit)):
        firstCond = i % firstNo == 0
        secondCond = i % secondNo == 0

        if i==0:
            print(0)
        elif firstCond and secondCond :
            print("FizzBuzz")
        elif firstCond:
            print("Fizz")
        elif secondCond:
            print("Buzz")
        else:
            print(i)

FizzBuzzFn(150,7,6)

