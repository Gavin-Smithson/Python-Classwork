#Gavin Smithson
#10/31/2022
#Spooky Cold
def tempcalc(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (celsius*9/5) + 35
    print('{}\t\t\t{}\t\t\t{}'.format(kelvin, celsius, fahrenheit))

def main():
    print('Kelvin\t\t\tCelsius\t\t\tFahrenheit')
    for temp in range (301):
        tempcalc(temp)






if __name__ == '__main__':
    main()