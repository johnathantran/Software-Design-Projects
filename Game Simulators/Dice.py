def main():
#  File: Dice.py
#  Description: Simulates roll of 2 dice and calculates the likelihood of rolling each numbers 2-12
#  Student's Name: Johnathan Tran
#  Student's UT EID: jht697
#  Course Name: CS 313E 
#  Unique Number: 51470
#
#  Date Created: 9/10/17
#  Date Last Modified: 9/15/2017

    import random
    random.seed(1314)

    # creating variables for each possible value of two dice
    trials = eval(input("How many times do you want to roll the dice? "))
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    sevens = 0
    eights = 0
    nines = 0
    tens = 0
    elevens = 0
    twelves = 0

    rolls = 0
    results_list = []

    # calculates the number of times that each sum is generated
    while rolls < trials:
        diceRoll_1 = random.randint(1,6)
        diceRoll_2 = random.randint(1,6)
        sums = diceRoll_1 + diceRoll_2
        
        if sums == 2:
            twos += 1
            
        if sums == 3:
            threes += 1

        if sums == 4:
            fours += 1

        if sums == 5:
            fives += 1

        if sums == 6:
            sixes += 1

        if sums == 7:
            sevens += 1

        if sums == 8:
            eights += 1
            
        if sums == 9:
            nines += 1

        if sums == 10:
            tens += 1

        if sums == 11:
            elevens += 1

        if sums == 12:
            twelves += 1

        rolls += 1

        
    results_list.append(twos)
    results_list.append(threes)
    results_list.append(fours)
    results_list.append(fives)
    results_list.append(sixes)
    results_list.append(sevens)
    results_list.append(eights)
    results_list.append(nines)
    results_list.append(tens)
    results_list.append(elevens)
    results_list.append(twelves)
    
    rolls += 1
  
    print("Results:", results_list)
    print()

    # scales down the size of the histogram if the number of rolls are over 100
    if trials > 100:
        results_list2 = []

        for item in results_list:
            item = (round(item * (100 / trials)))

            results_list2.append(item)
        results_list = results_list2
        
    # variable 'most' designates the highest point of the graph    
    most = max(results_list)   

    # creates a list that shows how many asterisks are displayed per column
    for idx,val in enumerate(results_list):
        count_list = []
            
        for nums in results_list:
            count = most - nums + 1
            if (count > 0):
                count += -1
                count_list.append(count)
                      
    height = 0
    
    while height < most:
        row = ""
        row += "| "
        i = 0

        # builds each row of the graph    
        for item in range(len(count_list)):
            if count_list[i] > 0:
                    row += "   "           
            if count_list[i] <= 0:
                     row += " * "               
            i += 1
                        
        print(row)  

        # keeps track of how many empty rows should be displayed before asterisks
        for item in range(len(count_list)):
            count_list[item] -= 1
                       
        height += 1

    # prints the x-axis of the histogram        
    print("+--+--+--+--+--+--+--+--+--+--+--+-")
    print("   2  3  4  5  6  7  8  9 10 11 12")
    print()

    """
    a = [4,3,2,1,0]
    maxx = max(a)
    counter = 0
    while counter < maxx:
        for i in range(len(a)):
            a[i] -= 1
        print(a)
        counter += 1
    """

 
main()
    
