import random

def generate_number():
    random.seed()
    generated_number = random.randint(0, 2000)
    print(generated_number)
    return generated_number

def get_user_guess():
    user_guess = 0
    while True:
        try:
            user_guess = int(input("Please guess your number: "))
        except ValueError:
            print("Please enter an integer")
            continue
        else:
            break
    return user_guess

def compare_guess_to_generated_number(generated_number):
    guess = get_user_guess()
    while guess != generated_number:
        if guess > generated_number:
            print("Number %d larger than required" % guess)
        elif guess < generated_number:
            print("Number %d smaller than required" % guess)
        guess = get_user_guess()
    print("Congratulations your guess {:d} is equal to the generated number {:d}!" .format(guess, generated_number))

def main():
    compare_guess_to_generated_number(generate_number())

if __name__ == "__main__":
    main()

