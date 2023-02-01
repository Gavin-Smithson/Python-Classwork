#Gavin Smithson
#10/10/2022
#Distance Loop
def main():
    #Declare
    i = 0
    current_hour = 0
    current_distance = 0
    #Ask for input
    hours = int(input('How many hours did you travel for? '))
    distance = int(input('How fast did you get in MPH? '))
    # Header
    print('Hours\t\t\tDistance Traveled')
    while i < hours:
        #Set i
        i = i + 1
        #calculate current hour and distance
        current_hour = current_hour + hours
        current_distance = current_distance + distance
        print('{}\t\t\t{}'.format(current_hour,current_distance))










if __name__ == "__main__":
    main()