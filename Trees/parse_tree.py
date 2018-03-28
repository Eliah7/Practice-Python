import stack as st
import node_representation as nr
import operator as op

def build_parse_tree(fp_exp):
    fp_list = fp_exp.split()
    p_stack = st.Stack()
    e_tree = nr.BinaryTree('')
    p_stack.push(e_tree)
    current_tree = e_tree

    for i in fp_list:
        if i == '(':
            current_tree.insert_left('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in ['+', '-', '*', '/', ')']:
            current_tree.set_root_val(int(i))
            parent = p_stack.pop()
            current_tree = parent
        elif i in ['+', '-', '*', '/']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError
    return e_tree

def evaluate(parse_tree):
    opers = {'+' : op.add, '-' : op.sub, '*' : op.mul, '/' : op.truediv}

    left = parse_tree.get_left_child()
    right = parse_tree.get_right_child()

    if left and right:
        fn = opers[parse_tree.get_root_val()]
        return fn(evaluate(left), evaluate(right))
    else:
        return parse_tree.get_root_val()

def print_exp(tree):
    str_val = ""
    if tree:
        str_val = '(' + print_exp(tree.get_left_child())
        str_val = str_val + str(tree.get_root_val())
        str_val = str_val + print_exp(tree.get_right_child()) + ')'
    return str_val

    
pt = build_parse_tree("( ( ( 45 + 6 ) * ( 10 + 5 ) ) * 3 )")
print(evaluate(pt))

print(print_exp(pt))
#pt.postorder()
