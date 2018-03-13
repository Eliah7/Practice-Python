"""A function to print out the factorial of a number"""

def fac_num(num):
    if num == 1:
        return 1
    else:
        return num*fac_num(num-1)

print(fac_num(5))
