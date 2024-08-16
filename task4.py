import random
import string

def generate_password(length, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """
    Generates a random password based on specified criteria.

    :param length: Length of the password
    :param use_upper: Include uppercase letters in the password
    :param use_lower: Include lowercase letters in the password
    :param use_digits: Include digits in the password
    :param use_symbols: Include symbols in the password
    :return: Generated password as a string
    """
    if length <= 0:
        print("Length must be a positive integer.")
        return ""

    # Define character sets
    upper = string.ascii_uppercase if use_upper else ""
    lower = string.ascii_lowercase if use_lower else ""
    digits = string.digits if use_digits else ""
    symbols = string.punctuation if use_symbols else ""

    # Combine all allowed characters
    all_chars = upper + lower + digits + symbols

    if not all_chars:
        print("No character types selected. Please select at least one character type.")
        return ""

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    # Get user input for password length
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Prompt user for complexity options
    use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    # Generate and display the password
    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()

