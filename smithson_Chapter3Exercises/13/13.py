def main():
    #Ask user for the weight
    lb = float(input('What is the weight of your package? '))
    #define different rates
    firstRate = 1.5
    secondRate = 3
    thirdRate = 4
    fourthRate = 4.75
    total = 0
    #Check for weight and calculate
    if lb <= 2:
        total = lb * firstRate
    elif lb > 2 and lb <= 6:
        total = lb * secondRate
    elif lb > 6 and lb <= 10:
        total = lb * thirdRate
    elif lb > 10:
        total = lb * fourthRate
    else:
        print('error')
    #print the output to the user
    print('Your total is {}'.format(total))


if __name__ == "__main__":
    main()