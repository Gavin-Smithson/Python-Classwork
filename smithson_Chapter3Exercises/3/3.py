def main():
    #Ask for age
    age = int(input('Please input your age '))
    #Flag
    found = False
    #Infant Age
    if age <= 1:
        print("You're a infant")
        found = True
    #Child Age
    if age > 1 and age < 13:
        print("You're a child")
        found = True
    #Teen Age
    if age >= 13 and age < 20:
        print("You're a teenager")
        found = False
    #Adult Age
    if age >= 20:
        print("You're an adult")
        found = True
    #Flag
    if found == False:
        print('Error')
if __name__ == "__main__":
    main()