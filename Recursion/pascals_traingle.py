import math as mt
def pascals_triangle(rows):
    my_row = []
    if rows == 1: # base case
        my_row.append([1])
        return(my_row)
    elif rows == 2:
        my_row = pascals_triangle(rows-1) + [[1,1]] 
        return my_row
    else:
        working_list = pascals_triangle(rows-1)
        this_row = []
        i = 0
        this_row.append(1)
        while i < len(working_list[rows-2])-1:
            this_row.append(working_list[rows-2][i] + working_list[rows-2][i+1])
            i = i + 1
        this_row.append(1)
        my_row = pascals_triangle(rows-1) + [this_row]
        return my_row
        
def display_triangle(rows):
    my_list = pascals_triangle(rows)
    tabs = rows  
    
    for each_list in my_list:
        tabs = tabs - 1  
        print_tabs(tabs)
        for each_elem in each_list:
            print(each_elem,end='  ')
        print()

    
def print_tabs(count):
    i = 0
    while i < count:
        print(end='  ')
        i = i + 1
       
display_triangle(10)
