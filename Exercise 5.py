#1/11/2023
#Gavin Smithson
#Charge account checker Reader
def main():
    #Open the file to read it
    fp = open('charge_accounts.txt')
    charge = fp.readlines()
    for index in range(len(charge)):
        charge[index] = charge[index].strip()
    account_num = input('Enter the account number to check for: ')

    #Check to see if a account exist and print
    if account_num in charge:
        print('The account entered does exist. ')
    else:
        print("The account entered does not exist. ")
    fp.close()
if __name__ == "__main__":
    main()