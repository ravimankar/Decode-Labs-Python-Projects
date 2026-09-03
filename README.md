import secrets
import string
import math


def get_password_length():
    while True:
        try:
            length = int(input("Enter desired password length (min 8): "))
            if length < 8:
                print("Password too short! Please enter 8 or more.")
                continue
            return length
        except ValueError:
            print("Invalid input! Please enter a number.")


def get_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ("y", "n"):
            return choice == "y"
        print("Please enter y or n.")


def get_user_preferences():
    print("Choose what to include in your password:")
    use_upper = get_yes_no("Include uppercase letters (A-Z)? (y/n): ")
    use_lower = get_yes_no("Include lowercase letters (a-z)? (y/n): ")
    use_digits = get_yes_no("Include numbers (0-9)? (y/n): ")
    use_symbols = get_yes_no("Include symbols (@,#,$)? (y/n): ")

    if not any([use_upper, use_lower, use_digits, use_symbols]):
        print("You must select at least one type! Defaulting to letters and digits.")
        use_upper, use_lower, use_digits = True, True, True

    return use_upper, use_lower, use_digits, use_symbols


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    selected_sets = []
    pool = ""

    if use_upper:
        pool += string.ascii_uppercase
        selected_sets.append(string.ascii_uppercase)
    if use_lower:
        pool += string.ascii_lowercase
        selected_sets.append(string.ascii_lowercase)
    if use_digits:
        pool += string.digits
        selected_sets.append(string.digits)
    if use_symbols:
        pool += string.punctuation
        selected_sets.append(string.punctuation)

    password_chars = [secrets.choice(s) for s in selected_sets]

    remaining = length - len(password_chars)
    password_chars += [secrets.choice(pool) for _ in range(remaining)]

    for i in range(len(password_chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_chars[i], password_chars[j] = password_chars[j], password_chars[i]

    return "".join(password_chars), len(pool)


def calculate_strength(length, pool_size):
    if pool_size <= 1:
        return 0
    return round(length * math.log2(pool_size), 2)


def main():
    print("=== Random Password Generator ===")
    length = get_password_length()
    use_upper, use_lower, use_digits, use_symbols = get_user_preferences()

    password, pool_size = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
    entropy = calculate_strength(length, pool_size)

    print("Your secure password:", password)
    print("Entropy strength:", entropy, "bits")

    input("Press Enter to exit...")


main()
