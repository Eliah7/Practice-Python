import stack as st

def infix_to_postfix(expression):
    op_stack = st.Stack()
    output = []
    operands = '+-/*'

    exp_list = expression.split(' ')
   
    
    for token in exp_list:
        if token is '(':
            op_stack.push(token)
        elif token in operands:
            op_stack.push(token)
        elif token is ')':
            while not op_stack.is_empty():
                poped = op_stack.pop()
                if poped != '(':
                    output.append(poped)
                    
        elif token not in operands:
            if token is not '(':
                output.append(token)
                
    return(output)

def print_postfix(the_string):
    the_list = infix_to_postfix(the_string)
    string = ""
    for each_token in the_list:
        string = string +' '+ str(each_token)
    print(string)

#(infix_to_postfix("( (A * B ) + ( C * D ) )"))
print_postfix("( A + B ) * C - ( D - E ) * ( F + G )")
