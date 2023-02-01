import random
def main():
    # Open the file to read it
    fp = open('8_ball_responses.txt')
    responses = fp.readlines()
    for index in range(len(responses)):
        responses[index] = responses[index].strip()
    #Loop for 8-ball questions
    while True:
        #Ask user if they would like to shake the e-ball also validate loop
        while True:
            end = input('Would you like to shake the magic 8-ball.\nYes [1] No [2] ')
            if end in ["1", "2"]:
                break
        #Check for flag
        if end == "2":
            break
        #Get the user to ask and showcase the response
        else:
            ask = input('What would you like to ask Mr 8-ball: ')
        #Use randint to generate a random response in the list
            print('You asked Mr 8-ball \n"{}".\nHis response is \n"{}"'.format(ask, responses[random.randint(0,11)]))
    #Close the txt
    fp.close()












if __name__ == "__main__":
    main()