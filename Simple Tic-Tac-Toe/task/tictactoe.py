# write your code here
def print_grid(matrix):
    print("-" * 9)
    for row_g in range(3):
        print("|", matrix[row_g][0], matrix[row_g][1], matrix[row_g][2], "|")
    print("-" * 9)


def analyzer(matrix):
    def check_diff(cells_str):
        return abs(cells_str.count("X") - cells_str.count("O"))

    def three_sym_in_row(m, sym):
        for j in range(3):
            if m[j][0] == sym and m[j][1] == sym and m[j][2] == sym:
                return True
            elif m[0][j] == sym and m[1][j] == sym and m[2][j] == sym:
                return True
            else:
                continue
        return False

    def three_sym_in_diagonal(m, sym):
        return m[0][0] == sym and m[1][1] == sym and m[2][2] == sym or \
            m[0][2] == sym and m[1][1] == sym and m[2][0] == sym

    input_seq = "".join(["".join(matrix[0]), "".join(matrix[1]), "".join(matrix[2])])

    if check_diff(input_seq) >= 2:
        print("check_diff")
        return "Impossible"
    elif three_sym_in_diagonal(matrix, "X"):
        return "X wins"
    elif three_sym_in_diagonal(matrix, "O"):
        return "O wins"
    elif three_sym_in_row(matrix, "X") and three_sym_in_row(matrix, "O"):
        print("XO_triple_in_rows")
        return "Impossible"
    elif three_sym_in_row(matrix, "X"):
        return "X wins"
    elif three_sym_in_row(matrix, "O"):
        return "O wins"
    elif input_seq.count(" "):
        return "Game not finished"
    elif input_seq.count("X") == 4 and input_seq.count("O") == 5 or \
            input_seq.count("O") == 4 and input_seq.count("X") == 5:
        return "Draw"
    else:
        return 'Go ahead!'


user_matrix = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print_grid(user_matrix)
result, i = [], 0

while i < 9:
    if i % 2:
        token = "O"
    else:
        token = "X"
    input_coordinates = input("Enter the coordinates:").split()
    if len(input_coordinates) != 2:
        print("You should enter two numbers!")
        continue
    if (not input_coordinates[0].isdigit() or not input_coordinates[1].isdigit()) and len(input_coordinates) == 2:
        print("You should enter numbers!")
        continue
    elif (int(input_coordinates[0]) not in [1, 2, 3]) or (int(input_coordinates[1]) not in [1, 2, 3]):
        print("Coordinates should be from 1 to 3!")
        continue
    else:
        row, col = input_coordinates
        if user_matrix[int(row)-1][int(col)-1] in ["X", "O"]:
            print("This cell is occupied! Choose another one!")
            continue
        else:
            user_matrix[int(row)-1][int(col)-1] = token
            print_grid(user_matrix)
            result.append(analyzer(user_matrix))
            if result[-1] == "Game not finished":
                i += 1
                continue
            else:
                break

print(result[-1])

# Garbage
#    outcomes = [
#       "Game not finished",
#        "Draw",
#        "X wins",
#        "O wins",
#        "Impossible",
#        'Go ahead!'
#    ]
# while True:
#    input_seq = input("Enter cells:").replace("_", " ")
#    if len(input_seq) <= 9:
#        break
# print("-" * 9)
# for i in range(9):
#    if i % 3 == 0:
#        print("| ", end="")
#    print(input_seq[i] + " ", end="")
#    if (i+1) % 3 == 0:
#        print("|")
# print("-" * 9)
# input_seq = " " * 9
# matrix = [[_ for _ in user_seq][i:i+3] for i in range(0, 9, 3)]
