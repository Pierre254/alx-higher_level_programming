#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Create a set to get unique elements
    uniq = set(my_list)
    
    # Initialize a variable to store the sum
    add = 0
    
    # Iterate over unique elements and add them to the sum
    for value in uniq:
        add += value
    
    # Return the sum
    return add
