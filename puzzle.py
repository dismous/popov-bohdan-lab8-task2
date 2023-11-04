import numpy as np
def validate_board(board):
    result = True
    matrix = []
    tmp_list = []
    for i in range(9):
        temp_array = []
        for j in range(len(board[i])):
            temp_array.append(board[i][j])
        matrix.append(temp_array)
    a = np.array(matrix)
    lin = []
    for k in range(9):
        tmp_list.append(a[:,k])                             #column
        for l in tmp_list:
            for t in l:
                if (t.isdigit()) and (int(t) <= 9) and (int(t) >= 1):
                    if t in lin:
                        result = False
                    else:
                        lin.append(t)
            lin = []
    tmp_list = []
    for k in range(9):
        tmp_list.append(a[k,:])                             #column
        for l in tmp_list:
            for t in l:
                if (t.isdigit()) and (int(t) <= 9) and (int(t) >= 1):
                    if t in lin:
                        result =  False
                    else:
                        lin.append(t)
            lin = []
    return result

bor = [
 "**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     9 5 ",
 " 6  83  *",
 "3   1  **",
 "  8  2***",
 "  2  ****"
]
print(validate_board(bor))
