#Gavin Smithson
#10/24/2022
#Pennies For Pay
def main():
    #Grab input and validate
    valid = False
    days = 0
    pennies = .01
    while not (valid):
        days = input("Enter number of days: ")
        # Check to make sure input is numeric and > 0
        if days.isnumeric():
            if int(days) > 0:
                days = int(days)
                valid = True
            else:
                print("Enter a number greater than 0")
        else:
            print("Invalid Data Type")
    #print headings
    print('Day\t\t\tTotal')
    #loop for pennies $$$
    for i in range (1,days+1):
        pennies *= 2
        #print outputs
        print('{}\t\t\t{}'.format(i, pennies))





if __name__ == "__main__":
    main()