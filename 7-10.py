#1/11/2023
#Gavin Smithson
#World Series Reader
def main():
    #Open the file to read it
    fp = open('WorldSeriesWinners.txt')
    winners = fp.readlines()
    for index in range(len(winners)):
        winners[index] = winners[index].strip()

    team = input('Enter the team to check for: ')
    #Check to see if a team won the world series
    if team in winners:
        print('Your team has won the world series')
        #If the team won see how many times
        wins = 0
        for t in winners:
            if t == team:
                wins += 1
        print("Your team has won {} world series".format(wins))
    else:
        print("Your team hasn't won.")
    fp.close()
    first_five = winners[:5]
    last_ten = winners[:-10]
    every_fifth_year = winners[::5]
    print('First five winners {}.\nLast ten {}.\nEvery fifth Year {}.'.format(first_five, last_ten, every_fifth_year))










if __name__ == '__main__':
    main()