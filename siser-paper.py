import random
import sys

# VARIABLES
CHOICE = ['paper' ,'rock','scissor']
COMPUTER_CHOICE = random.choice(CHOICE)
PLAYER_CHOICE = input("ENTER ROCK ,PAPER ,SISER :").lower()

# DICT FOR ...
actions = {
    "r":  f"You chose rock and computer chose {COMPUTER_CHOICE}",
    "p": f"You chose paper and computer chose {COMPUTER_CHOICE}",
    "s": f"You chose scissor and computer chose {COMPUTER_CHOICE}"
}

# actions.get(CHOICE, "Invalid choice"))

#CORE
def rock_paper_game():
        
        if PLAYER_CHOICE[0] == COMPUTER_CHOICE[0]:
            print("DRAW :DRAW")
            sys.exit()

        elif (PLAYER_CHOICE[0] == 'p' and COMPUTER_CHOICE[0] == 'r') or \
            (PLAYER_CHOICE[0] == 'r' and COMPUTER_CHOICE[0] == 's') or \
            (PLAYER_CHOICE[0] == 's' and COMPUTER_CHOICE[0] == 'p'):
            print(actions.get(PLAYER_CHOICE[0]), ": WIN")

        else:
            print(": LOOSER")


if __name__ == "__main__":
    rock_paper_game()