import re

def check_length(password):
    min_length = 8
    return len(password) >= min_length

def check_uppercase(password):
    return any(char.isupper() for char in password)

def check_lowercase(password):
    return any(char.islower() for char in password)

def check_digits(password):
    return any(char.isdigit() for char in password)

def check_special_characters(password):
    special_characters = "!@#$%^&*()-=_+[]{}|;':\",./<>?"
    return any(char in special_characters for char in password)

def password_strength_checker(password):
    strength = 0
    criteria = [check_length, check_uppercase, check_lowercase, check_digits, check_special_characters]

    for check in criteria:
        if check(password):
            strength += 1

    if strength == 1:
        return "Very Weak"
    elif strength == 2:
        return "Weak"
    elif strength == 3:
        return "Moderate"
    elif strength == 4:
        return "Strong"
    elif strength == 5:
        return "Very Strong"

if __name__ == "__main__":
    password = input("Enter a password: ")
    strength = password_strength_checker(password)
    print("Password strength: ", strength)
