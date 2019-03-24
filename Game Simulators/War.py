#  File: War.py
#  Description: Simulates the card game War
#  Student's Name: Johnathan Tran
#  Student's UT EID: jht697
#  Course Name: CS 313E 
#  Unique Number: 54170
#
#  Date Created: 9/29/2017
#  Date Last Modified: 10/6/2017



# creates class Card with attributes rank and suit
class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return(str(self.rank) + self.suit)
    
class Deck:
    
    # creates card objects and puts them into a deck
    def __init__(self):
        
        self.cardList = []
        suits_list = ["C", "D", "H", "S"]
        ranks_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        for suit in suits_list:
            for rank in ranks_list:
                card = Card(rank,suit)
                c = card.rank + card.suit
                self.cardList.append(c)

    # shuffles the deck    
    def shuffle(self,cardList):
        
        cardList = self.cardList
        import random
        random.seed(15)
        random.shuffle(self.cardList)
        
    # deals a card to each player from the deck
    def dealOne(self,Player):
        
        cardList = self.cardList
        dealtCard = self.cardList.pop(0)
        Player.hand.append(dealtCard)
        Player.handTotal += 1

    # gives the order of cards in the deck
    def __str__(self):
        
        string = ""
        i = 0
        while i <= 51:
            # organizes the deck into 4 rows
            if i % 13 == 0:
                string += "\n"
            string += " "
            string += str(self.cardList[i])
            i += 1
        return string

# creates the players with attributes hand and number of cards in hand
class Player:
    
    def __init__(self,hand,handTotal):
        self.hand = []
        self.handTotal = 0

    def __str__(self):
        string = ""
        
        i = 0
        while i < len(self.hand):
            if (i % 13 == 0) and (i != 0):
                string += '\n'
            string += " "
            string += str(self.hand[i])
            i += 1
        return string

# War game function
def playGame(cardDeck,player1,player2):

    # n is the round number
    n = 1

    # keeps the game running as long as both players still have cards in their hands
    handNotEmpty = True
    while handNotEmpty:
        
        print("\n\n\nROUND " + str(n) + ":")
        p1card = player1.hand.pop(0)
        p2card = player2.hand.pop(0)
        
        print("Player 1 plays:  " + p1card)
        print("Player 2 plays:  " + p2card)

        # gets the rank of the cards
        c1 = p1card[0]
        c2 = p2card[0]
        
        # create a dictionary of values for face cards and 10
        d = {}
        d['A'] = 14
        d['K'] = 13
        d['Q'] = 12
        d['J'] = 11
        d['1'] = 10

        # adds values of number cards to the dictionary
        for i in range(2,10):
            d[str(i)] = i

        # if player 1 has a higher card value than player 2, they win the other card
        if d[c1] > d[c2]:
            print("\nPlayer 1 wins round " + str(n) + ": " + p1card + " > " + p2card + "\n")
            player1.hand.append(p1card)
            player1.hand.append(p2card)
            player1.handTotal += 1
            player2.handTotal -= 1

        # if player 2 has a higher card value than player 1, they win the other card
        if d[c2] > d[c1]:
            print("\nPlayer 2 wins round " + str(n) + ": " + p2card + " > " + p1card + "\n")
            player2.hand.append(p1card)
            player2.hand.append(p2card)
            player2.handTotal += 1
            player1.handTotal -= 1
            
        # if both players have cards of equal value, initiate war
        if d[c2] == d[c1]:

            # players draw 3 cards face down again if face up cards are equal
            while d[c1] == d[c2]:
                print("\nWar starts:  " + p1card + " = " + p2card)

                # creates the piles where players will place their war cards
                WarPile1 = []
                WarPile2 = []
                
                # players both put 3 cards face down in the war pile
                for i in range(3):
                    p1War = player1.hand.pop(0)
                    print("Player 1 puts " + p1War + " face down")
                    WarPile1.append(p1War)

                    p2War = player2.hand.pop(0)
                    print("Player 2 puts " + p2War + " face down")
                    WarPile2.append(p2War)
                
                # players both play a 4th card face up and compare values
                p1card4 = player1.hand.pop(0)
                p2card4 = player2.hand.pop(0)
                print("Player 1 puts " + p1card4 + " face up")
                print("Player 2 puts " + p2card4 + " face up\n")

                c1 = p1card4[0]
                c2 = p2card4[0]

            # case if player 1 wins war
            if d[c1] > d[c2]:
                print("\nPlayer 1 wins round " + str(n) + ": " + p1card4 + " > " + p2card4 + "\n")

                player1.hand.append(p1card)         
                player1.hand += WarPile1
                player1.hand.append(p1card4)
                player1.hand.append(p2card)
                player1.hand += WarPile2
                player1.hand.append(p2card4)
                player1.handTotal += 5
                player2.handTotal -= 5

            # case if player 2 wins war  
            if d[c2] > d[c1]:
                print("\nPlayer 2 wins round " + str(n) + ": " + p2card4 + " > " + p1card4 + "\n")

                player2.hand.append(p1card)
                player2.hand += WarPile1
                player2.hand.append(p1card4)
                player2.hand.append(p2card)
                player2.hand += WarPile2
                player2.hand.append(p2card4)
                player2.handTotal += 5
                player1.handTotal -= 5  

        # displays current hands after each round                  
        print("Player 1 now has " + str(player1.handTotal) + " card(s) in hand:")
        print(str(player1))
        print()
        print("Player 2 now has " + str(player2.handTotal) + " card(s) in hand:")
        print(str(player2))

        n += 1

        # checks if either player has empty hands
        if player1.handTotal == 0 or player2.handTotal == 0:
            handNotEmpty = False            
        
        
def main():

    # displays the initial card deck
    cardDeck = Deck()
    print("Initial deck: ")
    print(cardDeck)

    # displays the card deck after it's been shuffled
    cardDeck.shuffle(cardDeck)
    print()
    print("Shuffled deck: ")
    print(cardDeck)
   
    # creates 2 instances of Player
    player1 = Player([],0)
    player2 = Player([],0)

    # deals a card to each player
    for i in range(26):
        cardDeck.dealOne(player1)
        cardDeck.dealOne(player2)

    print("\nInitial hands: ")
    print("Player 1:" + str(player1))
    
    print("\nPlayer 2:" + str(player2))
    
    playGame(cardDeck,player1,player2)

    if player2.handTotal == 0:
        print("\n\nGame over.  Player 1 wins!")
    else:
        print("\n\nGame over.  Player 2 wins!")
        
    print("\nFinal hands:")
    print("Player 1:" + str(player1))
    print("Player 2:" + str(player2))

main()
