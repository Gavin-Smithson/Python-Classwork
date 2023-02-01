square = [[4,9,2],[3,5,7],[8,1,6]]

#def sodoku_input:
 #   square = [[],[],[],]
 #   try:
  #      input('Enter a number for')
def sudoku_check():
    num_rows = 3
    num_cols = 3
    good_rows = 0
    for row in range(num_rows):
        total = 0
        for col in range(num_cols):
            total += (square[row][col])
            if total == 15:
                good_rows += 1
                total = 0

    for row in range(num_rows):
        col = row
        total += square[row][col]
        if total == 15:
            good_rows += 1
            total = 0
    length_col = num_cols - 1
    for row in range(num_rows):
        total += (square[row][length_col])
        length_col -= 1
        if total == 15:
            good_rows += 1
            total = 0


    print(good_rows)
    if good_rows == 5:
        print('magic square is magic')
    else:
        print('no magic')

def main():
    sudoku_check()






if __name__ == "__main__":
    main()