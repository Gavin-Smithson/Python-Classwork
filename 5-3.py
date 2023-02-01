#Gavin Smithson
#10/2/2022
#Math Quiz Code
import random
def validate_pos_int(prompt, error):
    while True:
        response = input(prompt)
        # Check to make sure input is numeric and > 0
        if response.isnumeric() and int(response) > 0:
                return int(response)
        else:
            print(error)
def main():
    num1 = random.randint(1, 999)
    num2 = random.randint(1, 999)
    print('{} + {} =_____'.format(num1, num2))
    answer = num1 + num2
    while True:
        guess = validate_pos_int('Enter your answer: ', 'Invalid entry')
        if guess == answer:
            print('You got it right! The answer is {}'.format(answer))
            break
        else:
            print('Incorrect')



if __name__ == "__main__":
    main()