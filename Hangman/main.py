def get_word_to_guess():
    # STUB
    return "barnacle"

def get_user_guess():
    user_guess = ''
    valid_input = False
    while not valid_input:
        user_guess = input("Please guess your letter: ")
        valid_input = len(user_guess) == 1 and user_guess.isalpha()
        if not valid_input:
            print("Please enter a single character")
    return user_guess

def calculate_number_of_attempts(word, difficulty_level=3):
    unique_chars = set()
    for char in word:
        unique_chars.add(char)
    return len(unique_chars) - difficulty_level

def main():
    investigated_word = get_word_to_guess()
    number_of_allowed_attempts = calculate_number_of_attempts(investigated_word)
    attempts_made = 0
    guesses = set()
    print("Number of letters in investigated word {:d}".format(len(investigated_word)))
    while attempts_made < number_of_allowed_attempts:
        was_guess_already_made = False
        guess = get_user_guess()
        was_guess_already_made = guess in guesses
        guesses.add(guess)
        print(guesses)
        if guess in investigated_word:
            result = ''.join([l if l in guesses else '_' for l in investigated_word])
            print(result)
            if result == investigated_word:
                print("Congratulations, you won!")
                break
        else:
            print(result)
            if not was_guess_already_made:
                attempts_made += 1
            print("Number of attempts left {:d}".format(number_of_allowed_attempts - attempts_made))


if __name__ == "__main__":
    main()