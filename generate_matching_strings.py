"""Up until now this program generates similar strings only
   with regards to occurance and not in order of occurance"""

import random as rn
import math as mt
import numpy as np

# conts
alphabets = 'abcdefghijklmnopqrstuvwxyz '

# Implementation
def to_list(the_string):
    """This function generates a list from the characters of a string"""
    mylist = []
    for each_ch in the_string:
        mylist.append(each_ch)
    return(mylist)


def generate_random_letters(my_string):
    """This function generates a string that is 27 characters
    long by choosing random letters from the 26 letters
    in the alphabet plus the space"""

    gen_string = ''
    letter_list = to_list(my_string)
 
    for i in range(27):
        random_index = rn.randint(0,26)
        gen_string += letter_list[random_index]

    return(gen_string)

def score_fn(first_string,second_string):
    """This function provides a measure of the difference btn two strings using cost functions"""
    return(1)

def gen_frequency(ch,string):
    """This function computes the frequency of each letter in a string and returns that int"""
    freq = 0
    for i in range(len(string)):
        if ch == string[i]:
            freq += 1
            
    return(freq)

def cosine_dist(v1,v2):
    """This function defines a cosine distance cost function
             x = cos (v1.v2) / (|v1||v2|)
    """
    distance = (np.dot(v1,v2))/((np.sqrt(np.dot(v1,v1)))*(np.sqrt(np.dot(v2,v2))))
    return(mt.abs(mt.cos(distance)))
    
def build_string_vector(the_string):
    """This function builds a vector with each component as the frequency of that letter"""
    vec = []
    for each_ch in alphabets:  # this ensures that all the vectors have the same size
        freq = gen_frequency(each_ch,the_string)
        vec.append(freq)

    return(vec)

def gen_until_equal(target,resourse_string):
    """This function generates a string until it matches the *target* string"""
    shakespeare_str = ''
    while True:
        shakespeare_str = generate_random_letters(resourse_string)
        my_vect = build_string_vector(shakespeare_str)
        target_vect = build_string_vector(target_sentence)
        score = cosine_dist(my_vect,target_vect)
        print("The String generated is %s with a cost of %.3f " % (shakespeare_str,score),end='\n')
        if score == 1:
            print("We have a match")
            break



# User calls
target_sentence = 'methinks it is a weasel'

gen_until_equal(target_sentence,alphabets)
