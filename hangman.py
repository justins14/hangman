import random

def get_guess(guessed):
    char = input("Guess a letter: ")
    while len(char) != 1 or not char.isalpha():
        print("\n")
        char = input("Not a valid input.  Please enter a letter: ")
    while char in guessed:
        print("\n")
        char = input("You've already guessed that.  Try again: ")
    return char.lower()

def set_solution(word_list):
    secure_random = random.SystemRandom()
    return list(secure_random.choice(word_list).lower())

def initialize_current_state(solution):
    current_state = []
    for i in range(len(solution)):
        current_state.append("__")
    return current_state

def set_current_state(solution, guess, current_state):
    if guess in solution:
        index_list = [i for i, x in enumerate(solution) if guess in x]
        for index in index_list:
            current_state[index] = guess
    return current_state

def clear_board():
    print("\n" * 100)
    print("--------Hangman--------")

def victory(stage, current_state, guessed):
    clear_board()
    draw_board(stage)
    draw_guessed(guessed)
    draw_word_field(current_state)
    print("Congratulations! You made {} wrong guesses!".format(stage))

def draw_loss(solution, guessed):
    clear_board()
    draw_board(5)
    draw_guessed(guessed)
    print("Sorry. Better luck next time.  Your word was \"{}\".".format("".join(solution)))
    print("\n")

def check_win(current_state):
    if "__" in current_state:
        return False
    else:
        return True

def check_loss(stage):
    if stage >= 5:
        return True
    else:
        return False

def draw_board(stage):
    board = ["",
            "___________        ",
            "|                  ",
            "|                  ",
            "|                  ",
            "|\                 ",
            "| \                ",
            "|  \               ",
            "-------------------",
            ""
            ]

    filled_board = ["",
                   "___________        ",
                   "|         |        ",
                   "|         |        ",
                   "|         O        ",
                   "|\       /|\       ",
                   "| \      / \       "
                   ]

    for i in range(stage):
        board[i+2] = filled_board[i+2]

    print("\n".join(board))

def draw_guessed(guessed):
    print("Already guessed: " + " ".join(sorted(guessed)))

def draw_word_field(current_state):
    print(" ".join(current_state))

def get_word_list():
    word_list = []
    with open("word_list.txt", "r") as f:
        for line in f:
            word_list.append(line.replace("\n",""))
    return word_list

#main
word_list = get_word_list()
solution = set_solution(word_list)
current_state = initialize_current_state(solution)
stage = 0
guessed = []
while not check_loss(stage):
    clear_board()
    draw_board(stage)
    draw_guessed(guessed)
    draw_word_field(current_state)
    guess = get_guess(guessed)
    guessed.append(guess)
    current_state = set_current_state(solution, guess, current_state)
    if guess not in solution:
        stage += 1
    if check_win(current_state):
        victory(stage, current_state, guessed)
        break

if check_loss(stage):
    draw_loss(solution, guessed)
