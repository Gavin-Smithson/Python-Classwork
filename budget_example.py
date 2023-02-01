# Program that allows the user to enter a monthly budget
# and expenses before telling them how much they went
# under or over

def main():
    # Budget input validation loop
    valid = False
    budget = 0
    while not(valid):
        budget = input("Enter monthly budget: ")
        #Check to make sure input is numeric and > 0
        if budget.isnumeric():
            if float(budget) > 0:
                budget = float(budget)
                valid = True
            else:
                print("You ain't got no mons")
        else:
            print("Invalid Data Type, go back to middle school")






    continue_adding = True
    while continue_adding:
        # Cost input validation loop
        valid = False
        cost = 0
        while not(valid):
            cost = input("Enter an expense or enter 'q' to quit: ")
            # Check to make sure input is numeric and > 0
            if cost.isnumeric():
                if float(cost) > 0:
                    cost = float(cost)
                    valid = True
                else:
                    print("You wish you were making money")
            elif cost == 'q':
                continue_adding = False
                valid = True
            else:
                print("Invalid Data Type, go back to middle school")

        # Ensures we do not compute on the quit case
        if continue_adding == True:
            # Subtract cost from budget
            budget = budget - cost
            #budget -= cost

    # Print the final budget
    print("Final Budget: {}".format(budget))



if __name__ == "__main__":
    main()