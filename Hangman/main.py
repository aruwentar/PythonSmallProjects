import re

def get_word_to_guess():
    # STUB
    return "barnacle"

def convert_word_to_char_list(word):
    char_list = list()
    for char in word:
        char_list.append(char)
    return char_list

def get_user_guess():
    user_guess = str()
    while True:
        user_guess = input("Please guess your letter: ")
        match = re.match("[a-zA-Z]", user_guess)
        if len(user_guess) != 1 or not match:
            print("Please enter a single character")
            continue
        else:
            break
    return user_guess

def calculate_number_of_attempts(word):
    unique_chars = set()
    for char in word:
        unique_chars.add(char)
    return len(unique_chars) - 3


def reveal_new_letters(listed_word, guess_indices, guess=[]):
        guess_indices.extend([i for i, e in enumerate(listed_word) if e == guess])
        word = str()
        for i in range(len(listed_word)):
            if i in guess_indices:
                word += listed_word[i]
            else:
                word += '_'
        return word

def main():
    investigated_word = get_word_to_guess()
    number_of_allowed_attempts = calculate_number_of_attempts(investigated_word)
    listed_word = convert_word_to_char_list(investigated_word)
    guess_indices = list()
    attempts_made = 0
    print("Number of letters in investigated word {:d}".format(len(investigated_word)))
    while attempts_made < number_of_allowed_attempts:
        guess = get_user_guess()
        if guess in listed_word:
            current_state = reveal_new_letters(listed_word, guess_indices, guess)
            print(current_state)
            if current_state == investigated_word:
                print("Congratulations, you won!")
                break
        else:
            current_state = reveal_new_letters(listed_word, guess_indices)
            print(current_state)
            attempts_made += 1
            print("Number of attempts left {:d}".format(number_of_allowed_attempts - attempts_made))


if __name__ == "__main__":
    main()