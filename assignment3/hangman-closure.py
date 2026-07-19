
def make_hangman(secret_word):
    secret_word = secret_word.lower()
    guesses = []

    def hangman_closure(letter):
        letter = letter.lower()

        guesses.append(letter)

        word = "".join(letter if letter in guesses else "_" for letter in secret_word)
        

        if "_" not in word:
            print(" ".join(word))
            print("You win!")
            return True
        else:
            print(" ".join(word))
            return False
    return hangman_closure



question = make_hangman(input("What is the secret word? "))

answer = input("Guess a letter: ")

question(answer)

win = False
while not win:
    answer = input("Guess a letter: ")
    win = question(answer)


