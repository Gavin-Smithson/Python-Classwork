def main():
    #Create a list for sales of each day of week
    days_of_week = 7
    weekly_sales = [0.0] * days_of_week
    total_sales = 0
    #Get the user input for sales for each day
    for index in range(len(weekly_sales)):
        while True:
            try:
                weekly_sales[index]  =  float(input("Enter the sales for day {:.0f}:  ".format(index + 1)))
                break
            except:
                print("Invalid sales")
        total_sales += weekly_sales[index]
        # Compute the sales total for the week
    print(total_sales)











if __name__ == "__main__":
    main()
