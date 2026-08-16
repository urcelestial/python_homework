
def make_hangman(secret_word):
    secret_word = secret_word.lower()
    guesses = []

    def hangman_closure(letter):
        letter = letter.lower()

        guesses.append(letter)

        word = "".join(letter if letter in guesses else "_" for letter in secret_word)
        print(word)

        if "_" not in word:
            return True
        return False
    return hangman_closure



question = make_hangman(input("What is the secret word? "))

win = False
while not win:
    answer = input("Guess a letter: ")
    win = question(answer)


