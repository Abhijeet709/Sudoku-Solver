# Sudoku-Solver
Python code to solve a 9X9 sudoku puzzle using backtracking

Description:
Sudoku is a logic puzzle game. The objective is to fill the 9x9 Sudoku grid with digits 1 to 9 such that each of these 9 digits appears in each row,
each column and each 3x3 sub-grid once any only once.

Input Method:
Input is provided using command line. For the 9X9 matrix, each row is entered with space separated elements.
To signify the vacant place zero is used. Ex - 1 2 3 4 0 0 7 0 0. 

Output:
If a solution is present for the puzzle it will print it out in the form of 9X9 matrix or else will print out "Solution not possible" message.

Programming Function Description:

1. def isSafe() - 
  >It takes matrix,a number,x and y coordinate of an empty postion as an arguments.
  >It decides whether the digit in question satisfy all the codition or not, if it does then it is placed in the matrix at a given position.
  >Return true if all conditions are met else will return false.
  
2. def getPos() - 
  >It takes matrix as an input.
  >It traverse through matrix and check for an empty position.
  >If an empty position is present it return its coordinates else return None to signify non existence of empty position.
  
3. def solver() - 
  >It takes matrix as an argument.
  >It return true if a solution is possible else false.
  >It is a recursive function which keep calling itself.
