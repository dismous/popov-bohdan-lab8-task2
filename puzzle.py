import numpy as np
def validate_board(board):
    
    temp_board = []
    for i in board:
        temp_board.append([i])
    m_board = np.matrix(temp_board)
    print(m_board)
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
