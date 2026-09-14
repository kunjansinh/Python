def check_password(password):
    has_upper = False
    has_lower = False
    has_digit = False

    for character in password:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True

    if len(password) < 8:
        return "Weak: password is too short."

    if has_upper and has_lower and has_digit:
        return "Strong password."

    return "Medium: add uppercase, lowercase and numbers."


password = input("Enter a password: ")

print(check_password(password))
