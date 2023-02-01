def list_calculations(list):
    mini = (min(list))
    maxi = (max(list))
    average = sum(list) / len(list)
    total = sum(list)
    return mini , maxi , average , total



def main():
    #Open txt and loop to create list
    fp = open('productsales.txt')
    sales = fp.readlines()
    for index in range(len(sales)):
        sales[index] = int(sales[index])
    #Call calculations function
    mini , maxi , average , total = list_calculations(sales)
    #Print minimum, maxmimum, average, and total in the correct order
    print('The total number of sales is ${:.2f}\nThe average of all sales is ${:.2f}\nThe lowest sales is ${:.2f}\nThe highest sales is ${:.2f}'
          .format(total, average, mini, maxi))
    #Close the file
    fp.close()









if __name__ == "__main__":
    main()