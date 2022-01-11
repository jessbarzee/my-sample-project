def main():
    board = ["",
        "1", "2", "3",
        "4", "5", "6",
        "7", "8", "9",
    ]
    print_board(board)

    location = int(input('Please pick a square where you would like to play (1-9):'))
    board[location] = 'X'
    print_board(board)

    location_2 = int(input('Please pick a square where you would like to play (1-9):'))
    board[location_2] = 'O'
    print_board(board)
    
    location_3 = int(input('Please pick a square where you would like to play (1-9):'))
    board[location_3] = 'X'
    print_board(board)

    location_4 = int(input('Please pick a square where you would like to play (1-9):'))
    board[location_4] = 'O'
    print_board(board)

    location_5 = int(input('Please pick a square where you would like to play (1-9):'))
    board[location_5] = 'X'
    print_board(board)

    location_6 = int(input('Please pick a square where you would like to play (1-9):'))
    board[location_6] = 'O'
    print_board(board)

    location_7 = int(input('Please pick a square where you would like to play (1-9):'))
    board[location_7] = 'X'
    print_board(board)

    location_8 = int(input('Please pick a square where you would like to play (1-9):'))
    board[location_8] = 'O'
    print_board(board)

    location_9 = int(input('Please pick a square where you would like to play (1-9):'))
    board[location_9] = 'X'
    print_board(board)

def print_board(board : list):
    print(f'{board[1]}| {board[2]}| {board[3]}')
    print('-+-+-')
    print(f'{board[4]}| {board[5]}| {board[6]}')
    print('-+-+-')
    print(f'{board[7]}| {board[8]}| {board[9]}')

# def is_there_a_winner(board):
#     pass

# def is_it_a_draw(board):
#     pass

# def is_game_over(board):
#     """
#     0 = not over
#     1 = X won
#     2 = Y won
#     3 = Draw
#     """
#     pass

if __name__ == '__main__':
    main()