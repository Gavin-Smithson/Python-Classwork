def main():
    answers = ("A",'C','D','D','D','D,','A','C','B','C',"A",'C','D','D','D','D,','A','C','B','C')
    choice = []
    with open('answers.txt', 'r') as fp:
        choice = fp.readlines()
    for index in range(len(choice)):
        choice[index] = choice[index].upper().strip()

    score = 0
    for index in range(len(choice)):
        if choice[index] == answers [index]:
            score += 5
    if score >= 75:
        print('You passed with a {}'.format(score))
    else:
        print('You failed')




if __name__ == "__main__":
    main()