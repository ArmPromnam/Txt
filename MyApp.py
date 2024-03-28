# ตัวแปรสำหรับเก็บสัญลักษณ์ของผู้เล่น
PLAYER_1 = "X"
PLAYER_2 = "O"

# ตัวแปรสำหรับเก็บกระดานเกม
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

# ฟังก์ชั่นสำหรับแสดงกระดานเกม
def print_board(board):
    for row in board:
        print(" ".join(row))

# ฟังก์ชั่นสำหรับตรวจสอบว่าช่องว่างบนกระดานเกมว่างหรือไม่
def is_valid_move(board, position):
    row, col = position
    return 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == " "

# ฟังก์ชั่นสำหรับเล่นเกม
def play_game(board):
    # กำหนดผู้เล่นเริ่มต้น
    current_player = PLAYER_1

    # วนลูปจนกว่าเกมจะจบ
    while True:
        # แสดงกระดานเกม
        print_board(board)

        # ขอตำแหน่งจากผู้เล่น
        position = input("ผู้เล่น {} เลือกตำแหน่ง (1-9): ".format(current_player))
        position = int(position) - 1

        # ตรวจสอบว่าตำแหน่งถูกต้อง
        if not is_valid_move(board, position):
            print("ตำแหน่งไม่ถูกต้อง กรุณาลองใหม่")
            continue

        # วางสัญลักษณ์บนกระดานเกม
        board[position // 3][position % 3] = current_player

        # ตรวจสอบว่าผู้เล่นชนะ
        if is_winning(board, current_player):
            print_board(board)
            print("ผู้เล่น {} ชนะ!".format(current_player))
            break

        # เปลี่ยนผู้เล่น
        current_player = PLAYER_1 if current_player == PLAYER_2 else PLAYER_2

        # ตรวจสอบว่าเกมเสมอ
        if is_board_full(board):
            print_board(board)
            print("เกมเสมอ")
            break

# ฟังก์ชั่นสำหรับตรวจสอบว่าผู้เล่นชนะ
def is_winning(board, player):
    # ตรวจสอบแนวตั้ง
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    
    # ตรวจสอบแนวนอน
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    
    # ตรวจสอบแนวทแยง
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# ฟังก์ชั่นสำหรับตรวจสอบว่ากระดานเกมเต็ม
def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

# เริ่มเล่นเกม
play_game(board)
