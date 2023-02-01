#Gavin Smithson
#10/24/2020
#Calorie Loop
def main():
    #Declare Minutes and Calorie Constants
    Minutes = 0
    Calories = 0
    #Print headings
    print('Minutes\t\t\tCalories')
    #Loop for counting miuntes
    for i in range (12):
        Minutes += 5
        #Calculate Calories
        Calories = 4.2 * Minutes
        #Print outputs
        print('{}\t\t\t{}'.format(Minutes, Calories))








if __name__ == "__main__":
    main()