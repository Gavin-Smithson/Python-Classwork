def main():
    # Open the file to read it
    fp = open('BoyNames.txt')
    boy_names = fp.readlines()
    for index in range(len(boy_names)):
        boy_names[index] = boy_names[index].strip().lower()

    fp = open('GirlNames.txt')
    girl_names = fp.readlines()
    for index in range(len(girl_names)):
        girl_names[index] = girl_names[index].strip().lower()
    #Ask user what they'd like to do and a name
    while True:
        choice = input('Enter "boy" to check for boy names,\t "girl" to check for girl names,\t "both" to check for both. ')
        choice = choice.lower()
        if choice in ["boy", "girl", "both"]:
            break

#Program checks for popular boy's name
    if choice == "boy":
        name = input('Please input a name. ')
        name = name.lower()
        if name in boy_names:
            print('{} was a popular name!'.format(name))
        else:
            print("{} wasn't a popular name!".format(name))

#Program checks for popular girl's name
    elif choice == "girl":
        name = input('Please input a name. ')
        name = name.lower()
        if name in girl_names:
            print('{} was a popular name!'.format(name))
        else:
            print("{} wasn't a popular name!".format(name))

#Program checks both girls and boy's name
    elif choice == 'both':
        boy_name = input("Please input your boy's name. ")
        boy_name = boy_name.lower()
        if boy_name in boy_names:
            print('{} was a popular name!'.format(boy_name))
        else:
            print("{} wasn't a popular name!".format(boy_name))
        girl_name = input("Please input your girl's name")
        girl_name = boy_name.lower()
        if girl_name in girl_names:
            print('{} was a popular name!'.format(girl_name))
        else:
            print("{} wasn't a popular name!".format(girl_name))
    fp.close()










if __name__ == "__main__":
    main()