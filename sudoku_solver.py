#Write a function that will solve a 9x9 Sudoku puzzle.
#The function will take one argument consisting of the 2D puzzle array,
#with the value 0 representing an unknown square.

#The Sudokus tested against your function will be "easy" (i.e. determinable;
#there will be no need to assume and test possibilities on unknowns) and can
#be solved with a brute-force approach.

import numpy as np
import copy

def sudoku(puzzle):
    puzzle_copy=copy.deepcopy(puzzle)
    check=np.array(puzzle_copy)
    check[check>0]=-1
    count=0
    
    while (np.sum(check))!=-81 and count <150:
        for number in range(1, 10):
            for row in range(10):
                try:
                    col_index=puzzle_copy[row].index(number)
                except:
                    col_index=-1
        
                #eliminate rows and columns and 3x3 blocks
                if(col_index>-1):
                    check[row,:]=-1
                    check[:,col_index]=-1
                    check[3*(row//3):3*(row//3+1), 3*(col_index//3):3*(col_index//3+1)]=-1
        
            #fill in if possible
            #scan 3x3 blocks
            update_flag=1

            while update_flag>0:
                update_flag=0
                for index1 in range(0, 3):
                    for index2 in range(0, 3):
                        block=check[3*index1:3*(index1+1), 3*index2:3*(index2+1)]
                        test=np.sum(block)
                        if(test==-8):
                            location=np.where(block==0)
                            answer_row=location[0][0]+index1*3
                            answer_col=location[1][0]+index2*3
                            puzzle_copy[answer_row][answer_col]=number
                            check[answer_row][answer_col]=-1
                            update_flag=1
            check=np.array(puzzle_copy)
            check[check>0]=-1                    
            count+=1

    return puzzle_copy
