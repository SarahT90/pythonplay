# It's time to duel!
import random

def roll_dice():
    dice_total = random.randint(1, 20)
    return dice_total

print("It's time to duel. Choose your fighter!")


player1 = input("Enter player 1's name:\n")
player2 = input("Enter player 2's name:\n")
print('Rolling for initiative!')

roll1 = roll_dice()
roll2 = roll_dice()

print(player1, 'rolled', roll1)
print(player2, 'rolled', roll2)
if (roll1 > roll2):
    print('Player 1 has initiative!')
elif (roll1 < roll2):
    print('Player 2 has initiative!')
else:
    print("It's a draw!")