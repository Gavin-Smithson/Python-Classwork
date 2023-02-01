#Gavin Smithson
#11/2/2022
#Rock Paper Sisscors
import random
def validate_pos_int(prompt, error):
    while True:
        response = input(prompt).lower()
        # Check to make sure input is numeric and > 0
        if response == 'rock' or response == 'scissors' or response == 'paper' or response == '5':
                return response
        else:
            print(error)
def main():
    while True:
        opp = random.randint(1, 3)
        guess = validate_pos_int('Rock, Paper, Or Scisscors? (Enter in lowercase): ', 'Invalid Entry')
        if guess == 'rock':
            guess = 1
        if guess == 'paper':
            guess = 2
        if guess == 'scissors':
            guess = 3
        if guess == 1 and opp == 3:
            print('You win! CPU was scissors'.format(opp))
            break
        elif guess == 2 and opp ==  1:
            print('You win! CPU was rock'.format(opp))
            break
        elif guess == 3 and opp == 2:
            print('You win! CPU was paper'.format(opp))
            break
        elif guess == opp:
            print('Tie! Go again!')
        elif guess == 5:
            print('You pulled a gun on him and he lost because you pulled a gun on him.')
        else:
            if opp == 1:
                opp = 'rock'
            if opp == 2:
                opp = 'paper'
            if opp == 3:
                opp = 'scissors'
            print('You lose! CPU was {}'.format(opp))






if __name__ == "__main__":
    main()