import random
import string


def generate_password(
    length, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True
):
    character_sets = ""
    if use_uppercase:
        character_sets += string.ascii_uppercase
    if use_lowercase:
        character_sets += string.ascii_lowercase
    if use_digits:
        character_sets += string.digits
    if use_symbols:
        character_sets += string.punctuation

    if not character_sets:
        print("Error: No character set selected for generating password.")
        return None

    password = "".join(random.choice(character_sets) for _ in range(length))
    return password


def get_yes_or_no_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")


def get_integer_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input <= 0:
                print("Password length must be greater than 0.")
            else:
                return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():
    try:
        length = get_integer_input("Enter the length of the password: ")
        use_uppercase = get_yes_or_no_input("Include uppercase letters? (y/n): ")
        use_lowercase = get_yes_or_no_input("Include lowercase letters? (y/n): ")
        use_digits = get_yes_or_no_input("Include digits? (y/n): ")
        use_symbols = get_yes_or_no_input("Include symbols? (y/n): ")

        password = generate_password(
            length, use_uppercase, use_lowercase, use_digits, use_symbols
        )
        if password:
            print("Generated Password:", password)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")


if __name__ == "__main__":
    main()
