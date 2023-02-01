#Gavin Smithson
#10/10/2022
#Tution Calculator
def main():
    #Set loop variables
    total_cost = 8000
    rate = 0.03
    tmp_cost = total_cost
    #Header
    print('Year\t\t\tCost')
    for year in range(5):
        tmp_cost = tmp_cost + (tmp_cost*rate)
        print('{}\t\t\t${:.2f}'.format(year,tmp_cost))

if __name__ == "__main__":
    main()