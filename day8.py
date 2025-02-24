#1
'''Create a function that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far.
wins get 3 points
draws get 1 point
losses get 0 points'''
#Examples
#football_points(3, 4, 2) ➞ 13
#football_points(5, 0, 2) ➞ 15
#football_points(0, 0, 1) ➞ 0

def football_points(wins, draws, losses):
		wins*=3
		draws*=1
		losses*=0
		return(wins+draws+losses)

wins=int(input("Enter no.of wins:"))
draws=int(input("Enter no.of draws:"))
losses=int(input("Enter no.of losses:"))
points=football_points(wins, draws, losses)
print(f"Total points:{points}")



#2
'''In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:

chickens = 2 legs
cows = 4 legs
pigs = 4 legs
The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a function that returns the total number of legs of all the animals.'''

#Examples
#animals(2, 3, 5) ➞ 36
#animals(1, 2, 3) ➞ 22
#animals(5, 2, 8) ➞ 50
