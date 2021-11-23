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
             it produce double grids and double the color regardsless of color.
             SOLVED CORRECTLY.
             
             solve_2204b7a8 -- This task requires to be given n amount of grids
             n colors in the boxes. 
             it then reads the colors in the input and then the output splits 
             into two so first half changes to the color of the intial color column 
             and the second half changes to the last column color.
             SOLVED CORRECTLY.
    '''
    return

#def solve_963e52fc(x):
    #x = np.tile(x,2)   
    #return x
   
#def solve_2204b7a8(x):
    #for i in range(len(x)):
        #for j in range(len(x[i])):
            #a = x[i][:len(x[i])//2]
            #b = x[i][len(x[i])//2:]
        #for i, element in enumerate(a):
            #if element.any() > 0:
                #a[i] = a[0]
        #for i, element in enumerate(b):
            #if element.any() > 0:
                #b[i] = b[-1] 
    #return x

def solve_f15e1fac(x):
       
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


