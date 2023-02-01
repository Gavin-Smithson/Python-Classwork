def main():
    #Input three test scores
    test1 = float(input('What is the first test score? '))
    test2 = float(input('What is the second test score? '))
    test3 = float(input('What is the third test score? '))
    #Process avg of test scores
    avg = (test1 + test2 + test3)/3
    #Output Avg
    print('Your average is {:.2f}'.format(avg))

    if avg >= 95:
        print('Congrats!')

if __name__=="__main__":
    main()