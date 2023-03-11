import random


#Class for players with name attribute to keep track of players, and a score attribute initialized as 0

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        
        
#Class for dice as an object with 6 "sides"
        
class Dice:
    def __init__(self):
        self.sides = 6
    
    #Roll function to get a random int between 1 and the number of sides(6)
    def roll(self):
        return random.randint(1, self.sides)        
    
#Class for the gameplay. Attributes are players, dice, and scores with winning score set to 100

class PigGame:
    def __init__(self, num_players):
        self.players = [Player(f"Player {i+1}") for i in range(num_players)]
        self.dice = Dice()
        self.current_player = 0
        self.current_score = 0
        self.winning_score = 25
    
    #Function to take input from players whether to roll or hold and bank points.
    def play(self):
        
        #While loop to keep playing until somebody wins
        while True:
            print("\n" + "=" * 20)
            print(f"It's {self.players[self.current_player].name}'s turn. Current score: {self.current_score}, Total score: {self.players[self.current_player].score}")
            choice = input("Press r to roll, h to hold and bank your score: ")
            
            #If/else to check whether the player wants to roll or hold, prints out information about the score
            
            
            #The first part of the if loop calls the roll method if the user input is r and checks to see if the roll is equal to 1
            #If the roll does equal 1, the current score for the turn is set to 0 and the next_player() method is called
            if choice.lower() == 'r':
                roll = self.dice.roll()
                print(f"{self.players[self.current_player].name} rolled a {roll}.")
                if roll == 1:
                    print(f"{self.players[self.current_player].name} rolled a Pig!! Your score is 0 this turn")
                    self.current_score = 0
                    self.next_player()
                    
                #Check if current player's total banked score + current score is equal to or greater than the winning score
                #The nested if loop prints out the current score for each roll that is not a 1, and breaks when a player reaches the winning score
                else:
                    self.current_score += roll
                    if self.players[self.current_player].score + self.current_score >= self.winning_score:
                        self.players[self.current_player].score += self.current_score
                        print(f"{self.players[self.current_player].name} wins!")
                        break
                    
                    else:
                        print(f"{self.players[self.current_player].name} current score: {self.current_score}")
                        
            #If the player chooses to bank points instead of rolling again, add the points to the player's total score and check whether it is >= the winning score
            #If the winning score isn't reached, the next player method is called
            elif choice.lower() == 'h':
                self.players[self.current_player].score += self.current_score
                print(f"{self.players[self.current_player].name} banked {self.current_score} points. Total score: {self.players[self.current_player].score}")
                self.current_score = 0
                if self.players[self.current_player].score >= self.winning_score:
                    print(f"{self.players[self.current_player].name} wins!")
                    break
                self.next_player()
                
            #I hit the wrong key during testing and nothing happened so I realized I needed to add another else to the loop for invalid input
            else:
                print("Invalid input. Please try again. Enter r to roll, h to hold and bank your score:")
                
                
    #Function to advance to next player and initialize current score for the turn as 0
    def next_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)
        self.current_score = 0

#Main function that asks the user how many players there are and calls the play method of the PigGame class

if __name__ == '__main__':
    num_players = int(input("Enter the number of players: "))
    game = PigGame(num_players)
    game.play()