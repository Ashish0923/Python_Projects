# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# 1. Rock beats scissors
# 2. Scissors beats paper
# 3. Paper beats rock

def winner(a, b):
    if a == 'rock':
        if b == 'rock':
            print('Nobody wins')
        elif b == 'paper':
            print('Player B wins')
        else:
            print('Player A wins')
    elif a == 'paper':
        if b == 'rock':
            print('Player A wins')
        elif b == 'paper':
            print('Nobody wins')
        else:
            print('Player B wins')
    else:
        if b == 'rock':
            print('Player B wins')
        elif b == 'paper':
            print('Player A wins')
        else:
            print('Nobody wins')


if __name__ == '__main__':
    while True:
        x = input("Type 'enter' to enter the game or type 'quit' to end the game: ")
        if x == 'quit':
            break
        elif x == 'enter' :
            player_a = input('Player A enter your input: ').lower()
            player_b = input('Player B enter your input: ').lower()
            winner(player_a, player_b)
        else:
            print("Didn't understand the command")

