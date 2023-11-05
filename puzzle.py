"""https://github.com/dismous/popov-bohdan-lab8-task2"""
import numpy as np
def validate_board(board):
    result = True
    matrix = []
    tmp_list = []
    color_y = []
    color_x = []
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
        tmp_list.append(a[k,:])                             #line
        for l in tmp_list:
            for t in l:
                if (t.isdigit()) and 0 <= int(t) <= 9:
                    if t in lin:
                        result =  False
                        break
                    else:
                        lin.append(t)
            lin = []
    
    for i in range(9): # checks color
        color_y.append(a[:, i].tolist())
        color_x.append(a[8 - i, :].tolist())
        color_x = color_x[0]
        color_y = color_y[0]
        yellow = color_x[i:(5 + i)]
        for j in color_y[4-i:9-i]:
            yellow.append(j)
        dub = []
        for k in yellow:
            if k.isdigit() and 0 <= int(k) <= 9:
                if k in dub:
                    result = False
                    break
                else:
                    dub.append(k)
        color_y = []
        color_x = []

    return result

