#!/usr/bin/python

import os, sys
import json
import numpy as np
import re

### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.

def my_func_doc_str():
    '''
    >>> Name :  Kelechi Ebereonwu
    >>> Student ID : 21230979
    
    >>> GitHub Repository: https://github.com/cosineK/ARC/tree/my_fix 
    
    >>> Tasks Descriptions:
             solve_963e52fc -- this task requires to be give an input matrix
             with n number of grid and n amount of colors in the grid.
             it produce double the grids and double the color regardsless of color.
             SOLVED CORRECTLY.
             
             solve_2204b7a8 -- This task requires to be given n amount of grids
             n colors in the boxes. 
             it then reads the colors in the input and then the output splits 
             into two so first half changes to the color of the intial color column 
             and the second half changes to the last column color.
             SOLVED CORRECTLY.
             
             solve_f15e1fac -- this task takes the input, made up of a base color box
             and another color box.
             The other color box will replace the black boxes in the grid in it's column or row 
             up as far as before the position of the base color box in the base color's box column or row
             e.g input = base color = 3
                         color box = 8
             input ARC, [0,0,0,0,0]
                        [0,0,0,0,8]
                        [0,2,0,0,0] 
             output ARC [8,8,0,0,0]
                        [0,0,8,8,8]
                        [0,2,0,0,0] 
             NOT SOLVED CORRECTLY.
             
    >>> Summary:
        The numpy library is an effective tool and definetly helped the structure of my coding, as most of the function I needed 
        that would have taken me few lines of code to excute, I can do in one line of code with the help of 
        numpy library.
        In regards to the commanlities; We only solving for x in all task,
        i.e the functions return only x, as y the output isn't available in run mode.
             
    '''
    return
def solve_f15e1fac(x):
    base_color = np.where(x==2)  #locate position of base color in the array and store
    increment_color = np.where(x==8) #locate position of the other color in the array and store
    increment_color = increment_color[0]+1 #go to next list in the array. i.e 
    
    for i in range(len(x)): #go through the entire grid
        x[increment_color]=8  #replace the black grids in the other color column
    return x

def solve_963e52fc(x):
    x = np.tile(x,2)  #repeat the color and grid size, twice 
    return x
   
def solve_2204b7a8(x):
    for i in range(len(x)):   #for the entire grid
        for j in range(len(x[i])):  #for the entire grid
            a = x[i][:len(x[i])//2]  #split first half of grid and store in a
            b = x[i][len(x[i])//2:]  ##split second half of grid and store in b
        for i, element in enumerate(a): #iterate through grid in the first half
            if element.any() > 0:  #if color exist
                a[i] = a[0]        #replace the the existing color box with new color box.
        for i, element in enumerate(b): #iterate through the second half
            if element.any() > 0:   ##if color exist
                b[i] = b[-1]        #replace the the existing color box with new color box.
    return x




def main():
    # Find all the functions defined in this file whose names are
    # like solve_abcd1234(), and run them.

    # regex to match solve_* functions and extract task IDs
    p = r"solve_([a-f0-9]{8})" 
    tasks_solvers = []
    # globals() gives a dict containing all global names (variables
    # and functions), as name: value pairs.
    for name in globals(): 
        m = re.match(p, name)
        if m:
            # if the name fits the pattern eg solve_abcd1234
            ID = m.group(1) # just the task ID
            solve_fn = globals()[name] # the fn itself
            tasks_solvers.append((ID, solve_fn))

    for ID, solve_fn in tasks_solvers:
        # for each task, read the data and call test()
        directory = os.path.join("..", "data", "training")
        json_filename = os.path.join(directory, ID + ".json")
        data = read_ARC_JSON(json_filename)
        test(ID, solve_fn, data)
    
def read_ARC_JSON(filepath):
    """Given a filepath, read in the ARC task data which is in JSON
    format. Extract the train/test input/output pairs of
    grids. Convert each grid to np.array and return train_input,
    train_output, test_input, test_output."""
    
    # Open the JSON file and load it 
    data = json.load(open(filepath))

    # Extract the train/test input/output grids. Each grid will be a
    # list of lists of ints. We convert to Numpy.
    train_input = [np.array(data['train'][i]['input']) for i in range(len(data['train']))]
    train_output = [np.array(data['train'][i]['output']) for i in range(len(data['train']))]
    test_input = [np.array(data['test'][i]['input']) for i in range(len(data['test']))]
    test_output = [np.array(data['test'][i]['output']) for i in range(len(data['test']))]

    return (train_input, train_output, test_input, test_output)


def test(taskID, solve, data):
    """Given a task ID, call the given solve() function on every
    example in the task data."""
    
    print(taskID)
    train_input, train_output, test_input, test_output = data
    print("Training grids")
    for x, y in zip(train_input, train_output):
        yhat = solve(x)
        show_result(x, y, yhat)
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        show_result(x, y, yhat)

        
def show_result(x, y, yhat):
    print("Input")
    print(x)
    print("Correct output")
    print(y)
    print("Our output")
    print(yhat)
    print("Correct?")
    if y.shape != yhat.shape:
        print(f"False. Incorrect shape: {y.shape} v {yhat.shape}")
    else:
        print(np.all(y == yhat))


if __name__ == "__main__": main()
print(my_func_doc_str.__doc__)


