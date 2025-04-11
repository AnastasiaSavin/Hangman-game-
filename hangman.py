import random, hangman_words, hangman_art

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
print(hangman_art.logo)

placeholder = "_" * len(chosen_word)
print('Word to guess:', placeholder)
display = '_' * len(chosen_word)
lives = 6
repeat = ''
while lives > 0:
    guess = input("Guess a letter: ").lower()

    if ord(guess) >= 97 and ord(guess) <= 122 and guess not in repeat:  # correct symbol

        repeat += guess
        flag = False

        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                flag = True
                display = display[:i] + guess + display[i + 1:]
            else:

                if not display[i].isalpha():
                    display = display[:i] + "_" + display[i + 1:]
                else:
                    continue
        if not flag:
            lives -= 1
            print('You guessed ', '"', guess, '"', ', that\'s not in the word. You lose a life.', sep='')
            print(hangman_art.stages[lives])
        print('Word to guess:', display)
        print('****************************',lives, '/6 LIVES LEFT****************************', sep='')
        if chosen_word == display:
            print('You win.')

    elif guess in repeat:
        print("You've already guessed ",'"',guess,'". ', "Try again.", sep='')
        print('****************************',lives, '/6 LIVES LEFT****************************', sep='')
    else:
        print("This is not a latin letter. Try again.")

        print('****************************',lives, '/6 LIVES LEFT****************************', sep='')
if chosen_word != display:

    print('***********************IT WAS ',chosen_word.upper(),'! YOU LOSE**********************',sep='')