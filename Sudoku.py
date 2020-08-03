#Input is taken row-wise,
#Each number is separated space
#use zero as an input for blank position
# Ex = 1 2 4 0 0 0 5 7 0
ls=[]
for i in range(9):
    ls.append(list(map(int,input().split())))


def isSafe(ls,num,i,j):
    
    #checking ith row
    for a in range(9):
        if ls[i][a] == num:
            return False
        
    #checking jth column
    for a in range(9):
        if ls[a][j] == num:
            return False
        
    #checking in 3X3 box
    X = (i//3)*3   #Starting row of a box
    Y = (j//3)*3   #Starting column of a box
    for a in range(X,X+3):
        for b in range(Y,Y+3):
            if ls[a][b] == num:
                return False
    return True
    
def getPos(ls):
    
    #traversing through matrix
    for i in range(len(ls)):
        for j in range(len(ls)):
            if ls[i][j]==0:
                return i,j
    #If no position is empty then return none
    return None

def solver(ls):
    
    #Base condition when whole matrix is full i.e. puzzle is complete
    if getPos(ls)==None:
        return True

    #If puzzle is incomplete
    else:
        i,j = getPos(ls)
        #For loop to try all the possible value
        for x in range(1,10):
            if isSafe(ls,x,i,j)==True:
                ls[i][j] = x
                #Checking if above entry will provide us solution or not
                if solver(ls)==True:
                    return True
                #Below position again set to zero as it provide no solution
                ls[i][j] = 0           
    return False

#Checking if there exist any solution for the puzzle or not
if solver(ls)==True:
    for i in range(9):
        for j in range(9):
            print(ls[i][j],end=' ')
        print()
else:
    print("Solution not possible")
        
