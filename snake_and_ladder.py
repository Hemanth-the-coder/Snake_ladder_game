import random

class player:   #A class for player to define their actions and properties
    def __init__(self, name):
        self.name=name
        self.counter=0
        # counter variable to keep track of the position of each player on the board 
    def names(self):
        return self.name  #returning name of the player
                         
    def throw(self):       #for generating possible number from 1-6 (dice)
        outcome=random.randint(1,6)
        return outcome

    def tracker(self, result):           #method used for updating the position of the player on board
        self.counter=self.counter+result
        if self.counter in ladder:
            print("wow, you got a ladder here \n")
            self.counter=ladder[self.counter]
        elif(self.counter in snakes):
            print("oops , its a snake , its time to run back \n")
            self.counter=snakes[self.counter]
        else:
            if(self.counter>100):
                self.counter=self.counter-result
        
#         --------------------------------------------------------- driver code starts here --------------------------------------------------------------------

no_of_players=int(input("please enter number of players: "))       #number of players 
players=[]
ladder={4:14, 9:31, 20:38, 28:84, 40:59, 63:81, 71:91}           #refer the jpeg image uploaded
snakes={99:78, 95:75, 93:73, 87:24, 62:18, 64:60, 54:34, 17:7}    #refer the jpeg image uploaded 
for i in range(no_of_players):
    print("name of player",i+1)
    players.append(player(input()))                       #creates a series of objects for player class 

print("all the best to all players \n")
print("press space bar to roll dice\n")
for i in players:
    print(i.names(), end=' ')
print("\n")
winners_declared=0                     #variable to check if a player whether any player has won 
print("lets start the game")
print("----------------------------------------------------------------------")
while(True):                                                              #game starts (iterative approach)
    for i in players:
        print("turn of "+i.names()+" to throw the die")
        throws=input(" ")
        result=i.throw()
        print("the outcome of the die is ", result, "\n")
        i.tracker(result)
        if (i.counter==100):
            print(i.names()+" won the match")
            winners_declared=1
            break                                     #terminates for loop 
        print("The position of "+ i.names()+" is " , i.counter)
        print("\n")
    if winners_declared==1:             #condition to end the game 
        break  
           

