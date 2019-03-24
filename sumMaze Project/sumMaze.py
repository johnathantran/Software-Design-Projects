#  File: sumMaze.py
#  Description: simulates solving a maze by reaching a given target sum
#  application using linked lists
#  Student's Name: Johnathan Tran
#  Student's UT EID: jht697
#  Course Name: CS 313E
#  Unique Number: 54170
#
#  Date Created: 11/15/2017
#  Date Last Modified: 11/18/2917

# class State
class State:

    def __init__(self,grid,history,row,col,sums):

        self.grid = grid
        self.history = history
        self.row = row
        self.col = col
        self.sums = sums

    def __str__(self):

        gridString = "      "

        for i in range(0,len(self.grid)):

            row = self.grid[i]

            # formats the grid
            for i in row:

                if (len(str(i)) == 1):
                    gridString += str(i) + "    "

                elif (len(str(i)) == 2):
                    gridString += str(i) + "   "

                else:
                    gridString += str(i) + "  "

            gridString += "\n      "

            startPoint = (self.row,self.col)

        gridString = gridString[:-7]

        return ("   Grid: \n" + gridString +
    "\n   history: " + str(self.history) +
    "\n   start point: " + str(startPoint) +
    "\n   sum so far: " + str(self.sums) + "\n")


# checks if each movement is valid given a direction
def isValid(thisState,direction):

    row = thisState.row
    col = thisState.col

    isValid = False

    # checks if moving RIGHT is valid
    if direction == 'right':

        print("No.  Can I move right?")

        if ((col + 1 < len(thisState.grid[row])) and
        (thisState.grid[row][col + 1] != 'X')):

            return True

    # checks if moving UP is valid
    if direction == 'up':

        print("No.  Can I move up?")

        if ((row - 1 >= 0) and
            (thisState.grid[row - 1][col] != 'X')):

            return True

    # checks if moving DOWN is valid
    if direction == 'down':

        print("No.  Can I move down?")

        if ((row + 1 < len(thisState.grid)) and
            (thisState.grid[row + 1][col] != 'X')):

            return True

    # try moving LEFT
    if direction == 'left':

        print("No.  Can I move left?")

        if ((col - 1 >= 0) and
            (thisState.grid[row][col - 1] != 'X')):

            return True

    return isValid


# creates function that determines movements throughout maze
def solve(thisState):

    print("Is this a goal state?")
    currentCoord = (thisState.row,thisState.col)

    # if the current state is a goal state
    if (currentCoord == goalCoord) and (thisState.sums == targetSum):

        print("Solution found!" + "\n" + str(thisState.history))
        return thisState.history

    if thisState.sums > targetSum:

        print("No.  Target exceeded: abandoning path")
        return None

    else:

        # if passes target sum
        # make a new state with previous location
        # try a different direction

        row = thisState.row
        col = thisState.col

        # try moving RIGHT
        if isValid(thisState,'right'):

            print("Yes!")

            # creates a new State
            newState = State(thisState.grid,thisState.history,row,
            col + 1,thisState.sums)

            # updates the path history
            location = int(newState.grid[newState.row][newState.col])
            newState.history.append(location)

            # updates the current sum
            num = int(newState.grid[newState.row][newState.col])
            newState.sums += num

            # updates current location by dropping a 'bread crumb'
            newState.grid[newState.row][newState.col] = 'X'

            print("\nProblem is now:")
            print(newState)

            result = solve(newState)
            if result != None:
                return result
            else:

                lastStep = newState.history.pop()
                newState.grid[newState.row][newState.col] = lastStep
                newState.sums -= lastStep

        # try moving UP
        if isValid(thisState,'up'):

            print("Yes!")

            # creates a new State
            newState = State(thisState.grid,thisState.history,row - 1,
            col,thisState.sums)

            # updates the path history
            print(str(newState.row) + " " + str(newState.col))
            location = int(newState.grid[newState.row][newState.col])
            newState.history.append(location)

            # updates the current sum
            num = int(newState.grid[newState.row][newState.col])
            newState.sums += num

            # updates current location by dropping a 'bread crumb'
            newState.grid[newState.row][newState.col] = 'X'

            print("\nProblem is now:")
            print(newState)

            result = solve(newState)
            if result != None:
                return result

            else:

                lastStep = newState.history.pop()
                newState.grid[newState.row][newState.col] = lastStep
                newState.sums -= lastStep


        # try moving DOWN
        if isValid(thisState,'down'):

            print("Yes!")

            # creates a new State
            newState = State(thisState.grid,thisState.history,row + 1,
            col,thisState.sums)

            # updates the path history
            location = int(newState.grid[newState.row][newState.col])
            newState.history.append(location)

            # updates the current sum
            num = int(newState.grid[newState.row][newState.col])
            newState.sums += num

            # updates current location by dropping a 'bread crumb'
            newState.grid[newState.row][newState.col] = 'X'

            print("\nProblem is now:")
            print(newState)

            result = solve(newState)
            if result != None:
                return result

            else:

                lastStep = newState.history.pop()
                newState.grid[newState.row][newState.col] = lastStep
                newState.sums -= lastStep

        # try moving LEFT
        if isValid(thisState,'left'):

            print("Yes!")

            # creates a new State
            newState = State(thisState.grid,thisState.history,row,
            col - 1,thisState.sums)

            # updates the path history
            location = int(newState.grid[newState.row][newState.col])
            newState.history.append(location)

            # updates the current sum
            num = int(newState.grid[newState.row][newState.col])
            newState.sums += num

            # updates current location by dropping a 'bread crumb'
            newState.grid[newState.row][newState.col] = 'X'

            print("\nProblem is now:")
            print(newState)

            result = solve(newState)
            if result != None:
                return result

            else:

                lastStep = newState.history.pop()
                newState.grid[newState.row][newState.col] = lastStep
                newState.sums -= lastStep

        # if no valid movements are available
        else:

            print("Couldn't move in any direction. That sucks. Backtracking.")
            return None


# opens the file and reads in maze data
f = open("mazedata.txt","r")

firstLine = f.readline().split()

# creates variables from data from first line
targetSum = int(firstLine[0])
gridRows = firstLine[1]
gridCols = firstLine[2]
startRow = int(firstLine[3])
startCol = int(firstLine[4])
endRow = int(firstLine[5])
endCol = int(firstLine[6])

goalCoord = (endRow,endCol)


def main():

    grid = []

    # logs the initial position
    startCoord = (startRow,startCol)

    print("Starting coords: " + str(startCoord) + "\nGoal Coords: " +
          str(goalCoord) + "\nTarget sum: " + str(targetSum) + "\n")

    # adds initial position to path history
    history = []
    # history.append(startCoord)

    # creates the grid
    for line in f:

        row = line.split()
        grid.append(row)

    # takes the starting value as the start sum
    startSum = int(grid[int(startRow)][int(startCol)])
    history.append(startSum)

    grid[startRow][startCol] = 'X'

    # creates the initial state
    startState = State(grid,history,startRow,startCol,startSum)

    print(startState)

    solve(startState)

main()
