# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

def game(num, correct_num,cnt):
    if num > correct_num:
        print('Too High')
    elif num < correct_num:
        print('Too Low')
    else:
        print('Exactly Right')


if __name__ == '__main__':
    import random
    cnt = 0
    rnd_num = random.randint(0, 9)
    while True:
        x = input("Type 'enter' to continue guessing the number or type 'quit' to end the game: ")
        if x == 'quit':
            break
        elif x == 'enter':
            guess_number = int(input('Enter your guess: '))
            game(guess_number, rnd_num,cnt)
            cnt = cnt + 1
        else:
            print("Didn't understand the command")
    print(cnt)
