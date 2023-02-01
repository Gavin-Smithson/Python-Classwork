def main():
    #Ask user for their color
    print('Welcome to the primary color mixer!')
    color1 = input('Please input first color ')
    color2 = input('Please input second color ')
    color1=color1.lower()
    color2=color2.lower()
    #Flag thing
    found = False
    #Purple Mix
    if color1 == 'red' and color2 == 'blue':
        print('Purple')
        found = True
    if color1 == 'blue' and color2 == 'red':
        print ('Purple')
        found = True
    #Orange Mix
    if color1 == 'red' and color2 == 'yellow':
        print('Orange')
        found = False
    if color1 == 'yellow' and color2 == 'red':
        print('Orange')
        found = True
    #Green Mix
    if color1 == 'blue' and color2 == 'yellow':
        print('Green')
        found = True
    if color1 == 'yellow' and color2 == 'blue':
        print('Green')
        found = True
    #Error thing
    if found == False:
        print ('error')

if __name__ == "__main__":
    main()