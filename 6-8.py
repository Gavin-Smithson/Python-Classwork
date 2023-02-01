def main():
    #Declare global vars to print later
    i = 0
    total = 0
    #Open the txt file
    fp = open("random_numbers.txt", "r")
    #Loop to read lines
    for line in fp:
        #convert line to int
        number = int(line)
        #Get accumlator vars
        i = i + 1
        total = total + number
    #Close the file
    fp.close()
    #Print outputs
    print('Total: {}\nI: {}'.format(total, i))






if __name__ == "__main__":
    main()