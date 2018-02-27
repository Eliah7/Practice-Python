import stack

def par_checker(symbol_string):
    s = stack.Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            elif symbol == ")":
                s.pop()
            else:
                balanced = False
        index = index + 1

    if balanced and s.is_empty():
        return True
    else:
        return False

print(par_checker('((()))'))
print(par_checker('()()()()()'))
