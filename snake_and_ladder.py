import random

class player:
    def __init__(self, name):
        self.name=name
        self.counter=0


    def names(self):
        return self.name

    def throw(self):
        outcome=random.randint(1,6)
        return outcome

    def tracker(self, result):

        self.counter=self.counter+result
        if self.counter in ladder:
            print("wow, you got a ladder here \n")
            self.counter=ladder[self.counter]
        elif(self.counter in snakes):
            print("oops , its a snake , its time to run back")
            self.counter=snakes[self.counter]
        else:
            if(self.counter>100):
                self.counter=self.counter-result


no_of_players=int(input("please enter number of players: "))
players=[]
ladder={4:14, 9:31, 20:38, 28:84, 40:59, 63:81, 71:91}
snakes={99:78, 95:75, 93:73, 87:24, 62:18, 64:60, 54:34, 17:7}
for i in range(no_of_players):
    print("name of player ",i+1)
    players.append(player(input()))

print("all the best to all players ")
for i in players:
    print(i.names(), end=' ')
print("\n")
winners_declared=0
print("lets start the game")
while(True):
    for i in players:
        print("turn of "+i.names()+" to throw the die")
        throws=input(" ")
        result=i.throw()
        print("the outcome of the die is ", result, "\n")
        i.tracker(result)
        if (i.counter==100):
            print(i.names()+" won the match")
            winners_declared=1
        
        print("The position of "+ i.names()+" is " , i.counter)
        print("\n")
    if winners_declared==1:
        break 
   

