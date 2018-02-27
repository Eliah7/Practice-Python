import stack

def par_checker(symbol_string):
    s = stack.Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "{([":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            elif symbol in ")]}":
                 top = s.pop()
                 if not matches(top,symbol):
                     balanced = False
            else:
                balanced = False
        index = index + 1

    if balanced and s.is_empty():
        return True
    else:
        return False

def matches(open, close):
   opens = "([{"
   closes = ")]}"
   return opens.index(open) == closes.index(close)


print(par_checker('{(})'))
print(par_checker('()()()()()'))
