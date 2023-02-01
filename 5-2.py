
def validate_pos_int():
    while True:
        response = input("Enter a number: ")
        # Check to make sure input is numeric and > 0
        if response.isnumeric() and int(response) > 0:
                return int(response)
        else:
            print("Invalid data type")




def main():
    cost = validate_pos_int()
    insurance = cost * .8
    print('You should insurance {:.2f}$'.format(insurance))





if __name__ == "__main__":
    main()