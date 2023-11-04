import numpy as np
def validate_board(board):
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
        tmp_list.append(a[:,k])
        for l in tmp_list:
            for t in l:
                if (t.isdigit()) and (int(t) <= 9) and (int(t) >= 1):
                    if t in lin:
                        return False
                    else:
                        lin.append(t)
    return tmp_list



    # temp_board = []
    # for i in board:
    #     temp_board.append([i])
    # valid_symbols = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '*'}
    
    # # Convert the input board to a NumPy matrix
    # m_board = np.matrix(temp_board)
    # f_board = m_board.flatten()
    # for i in m_board:
    #     for j in i[0]:
    #         for k in j[0]:

        #for j in range(9):
            
    # Check for duplicates in the row and column
    # if len(set(row)) != 9 or len(set(col)) != 9:
    #     return False  # Duplicates found in rows or columns

board = [
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
print(validate_board(board))
