#Gavin Smithson
#10/19/2022
#Population Simulation
def main():
    #Get daily increase
    daily_increase = 0
    valid = False
    while not (valid):
        daily_increase = (input('How much will the population increase each day? (Please Input a Percent): '))
        # Check to make sure input is numeric and > 0
        daily_increase = daily_increase.replace("%", "")
        if daily_increase.isnumeric():
            if float(daily_increase) > 0:
                daily_increase = float(daily_increase)
                daily_increase = daily_increase/100
                valid = True
            else:
                print("Please input a number greater than 0")
        else:
            print("Invalid Data Type")
    #Get days
    days = 0
    valid = False
    while not (valid):
        valid = False
        days = input("Enter number of days: ")
        # Check to make sure input is numeric and > 0
        if days.isnumeric():
            if float(days) > 0:
                days = int(days)
                valid = True
            else:
                print("Please input a number greater than 0")
        else:
            print("Invalid Data Type")
    #Get starting pop
    starting_population = 0
    valid = False
    while not (valid):
        valid = False
        starting_population = input("Enter starting population: ")
        # Check to make sure input is numeric and > 0
        if starting_population.isnumeric():
            if float(starting_population) > 0:
                starting_population = int(starting_population)
                valid = True
            else:
                print("Please input a number greater than 0")
        else:
            print("Invalid Data Type")
    print('{} {}'.format(starting_population,daily_increase,))
    print('Day\tApprox Population')
    for i in range (1 ,days+1):
        print('{}\t{}'.format(i, starting_population))
        starting_population = starting_population + (starting_population * daily_increase)








if __name__ == "__main__":
    main()