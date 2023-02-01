#Gavin Smithson
#10/24/2022
#Global Warming Program
def main():
    #Declare sea level
   sea_level = 0
    #Print Headers
   print('Year\t\t\tAmount Risen')
    #loop for levels
   for i in range (1, 26):
       sea_level += 1.6
       print('{}\t\t\t{:.3}'.format(i, sea_level))





if __name__ == "__main__":
    main()