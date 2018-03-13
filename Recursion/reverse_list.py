"""This function reverses the list given recursively """

def reverse_list(the_list):
    if len(the_list) == 1:    # Base case
        return(the_list)
    else:
        return(reverse_list(the_list[1:]) + [the_list[0]])
    
print(reverse_list([1,2,3,4,5,6,7,8,9,10,11]))
