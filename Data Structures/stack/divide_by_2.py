import stack as st

def divide_by_2(dec_number,base=2):
    digits = "0123456789ABCDEF"
    rem_stack = st.Stack()

    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)
        dec_number = dec_number // base

    bin_string = ''
    while not rem_stack.is_empty():
        bin_string = bin_string + digits[rem_stack.pop()]

    return bin_string

print(divide_by_2(834345635,15))
print(divide_by_2(25,2))
