sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

def sudoku_func(*args) :
    for i in range(len(sudoku)):
        line = ""
        if i == 0 or i == 3 or i == 6 :            
            print("- - - - - - - - - - - -")
        for j in range(len(sudoku[i])):
            if j == 3 or j == 6 :
                line += " | "
            line += str(sudoku[i][j]) + " "
        print(line)
    print("- - - - - - - - - - - -") 
print(sudoku_func(sudoku))