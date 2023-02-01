def main():
    #Open list and loop to create year list
    fp = open('USPopulation.txt')
    pop = fp.readlines()
    for index in range(len(pop)):
        pop[index] = int(pop[index])
    #Create list for the dif in the years
    changes = []
    year = []
    i = 0
    for index in range(1, len(pop)):
        changes.append(pop[index] - pop[index - 1])
        year.append(1951 + i)
        i += 1
    min_index = changes.index(min(changes))
    max_index = changes.index(max(changes))

    print('The average rate of change {}'.format(sum(changes) / len(changes)))
    print('The minimum year of change {}'.format(year[min_index]))
    print('The maximum year of change {}'.format(year[max_index]))




if __name__ == "__main__":
    main()