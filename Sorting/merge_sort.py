import math as mt

def merge_sort_slice(a_list):
    print("Splitting ", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]  # slicing is O(k) so use indices instead
        right_half = a_list[mid:]

        merge_sort_slice(left_half)
        merge_sort_slice(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):  # before one list is empty
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1
            else:
                a_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half): # if the right half is empty
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half): # if the left half is empty
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1
        print("Merging ",a_list)

def merge(a_list, p, q, r):
    n_left = q - p + 1
    n_right = r - q
 
    # create temp arrays
    left_half = [0] * (n_left)
    right_half = [0] * (n_right)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0 , n_left):
        left_half[i] = a_list[p + i]
 
    for j in range(0 , n_right):
        right_half[j] = a_list[q + 1 + j]
    #right_half.append(None)

    i = 0
    j = 0
    k = p # problem was here

    while i < n_left and j < n_right:  # before one list is empty
        if left_half[i] < right_half[j]:
            a_list[k] = left_half[i]
            i = i + 1
        else:
            a_list[k] = right_half[j]
            j = j + 1
        k = k + 1

    while i < n_left: 
        a_list[k] = left_half[i]
        i = i + 1
        k = k + 1

    while j < n_right: # if the left half is empty
        a_list[k] = right_half[j]
        j = j + 1
        k = k + 1
            
  

def merge_sort(a_list, p, r):
    if p < r:
        q = mt.floor((p+(r-1)) / 2)
        
        merge_sort(a_list, p, q)
        merge_sort(a_list, q + 1, r)
        merge(a_list, p, q, r)
        
        
    
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(a_list, 0, len(a_list) - 1)
print(a_list)
