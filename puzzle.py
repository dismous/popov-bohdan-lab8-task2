import numpy as np
def validate_board(board):
    valid_symbols = [1, 2, 3, 4, 5, 6, 7, 8, 9, '*', " ", '1', '2', '3',\
                      '4', '5', '6', '7', '8', '9']
    valid_symbols_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, '1', '2', '3',\
                      '4', '5', '6', '7', '8', '9']
    temp_board = []
    temp_list = []
    f_l = []
    for i in board:
        temp_board.append([i])
    m_board = np.matrix(temp_board)
    for i in range(len(m_board)):
        for j in str(m_board[i]):
            if j in valid_symbols_1:
                f_l.append(int(j))
        print(f_l)
        
        for k in range(9):
            f_l.count(k)
                
    return '1'

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
