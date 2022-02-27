import random

slowa_do_wyboru = ["krowa", "kot", "pies"]

word = random.choice(slowa_do_wyboru)

def wisielec(word):
    stages = [
                "         ",
              "_________",
              "|       | ",
              "|       0 ",
              "|      /|\ ",
              "|      / \ ",
              ]
    win = False
    wrong = 0
    letters = list(word)
    board = ["_"] * len(word)
    print("gra w wisielca")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Odgadnij litere: "
        guess = input(msg)
        if guess in letters:
            position = letters.index(guess)
            board[position] = guess
            letters[position] = '$%&'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("Wygrales!")
            print("masz racje haslo to" + " "  + ("".join(board)))
            win = True
            break
    if win == False:
        #print("\n".join(stages[0: e]))
        print("\n")
        print("przegrales, slowem bylo " + " " + word)


wisielec(word)
