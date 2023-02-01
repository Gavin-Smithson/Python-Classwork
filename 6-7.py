import random
import validate
def main():
    #Open/Create the numbers file
    fp = open("random_numbers.txt", "w")
    #Ask user for how many num
    r = validate.pos_int("Enter how many random numbers you would like to generate: ", "Error")
    #loop to create and write random nums
    for i in range(r):
        random_num = random.randint(1, 500)
        fp.write("{}\n".format(random_num))
    #Close the txt file
    fp.close()
if __name__ == "__main__":
    main()