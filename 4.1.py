#Gavin Smithson
#10/10/2022
#Bug Collector
def main():
    #Set iteration and total
    day = 0
    total = 0
    #Declare loop
    while day < 5:
        #ask for num of bugs for day
        num_bugs = int(input('Enter the number of bugs for day {}'.format(day)))
        #Add the total num of bugs to the running total
        total = total + num_bugs
        day = day + 1
    #Output the total number of bugs
    print('The total number of bugs after {} days is {}'.format(day, total))





if __name__ == "__main__":
    main()