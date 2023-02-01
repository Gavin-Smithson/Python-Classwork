#Gavin Smithson
#10/17/2022
#Nested Loop yearly rainfall
def main():
    total_rainfall = 0
    #Rainfall input validation loop
    valid = False
    num_years = 0
    while not (valid):
        num_years = input("How many years do you want to track?: ")
        # Check to make sure input is numeric and > 0
        if num_years.isnumeric():
            num_years = int(num_years)
            if (num_years) > 0:
                valid = True
            else:
                print("Error: Invalid Number")
        else:
            print("Error: Invalid Data Type")
    for year in range(num_years):
        for month in range(1,13):
            cur_rainfall = float(input('Please input the current months rainfall {}/12'.format(month)))
            while not (valid):
                cur_rainfall = input('Please input the current months rainfall {}/12: '.format(month))
                # Check to make sure input is numeric and > 0
                if cur_rainfall.isnumeric():
                    cur_rainfall = float(cur_rainfall)
                    if (cur_rainfall) > 0:
                        valid = True
                    else:
                        print("Error: Invalid Number")
                else:
                    print("Error: Invalid Data Type")
            total_rainfall = total_rainfall + cur_rainfall
    total_months = (num_years*12)
    rainfall_avg = total_rainfall/total_months
    print('It rained {} inches over the course of {} years. The average rainfall for {} months is {}'.format(total_rainfall,num_years,total_months,rainfall_avg))

if __name__ == "__main__":
    main()