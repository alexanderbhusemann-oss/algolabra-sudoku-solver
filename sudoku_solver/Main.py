def read_board():
    board = []
    print("Enter each row as 9 digits; use 0 for an empty cell.")

    for row_number in range(1, 10):
        while True:
            user_entry = input(f"Row {row_number}/9: ").strip()

            if len(user_entry) == 9 and all(
                character in "0123456789" for character in user_entry
            ):
                board.append([int(character) for character in user_entry])
                break

            print("Please enter exactly 9 digits from 0 to 9.")

    return board



def enter_board():

    board = read_board()
    print(board)



if __name__ == "__main__":
    enter_board()