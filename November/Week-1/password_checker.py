import string


def check_password_strength(password: str) -> tuple[str, list[str]]:
    missing = []

    if len(password) < 8:
        missing.append("at least 8 characters")
    if not any(ch.isupper() for ch in password):
        missing.append("an uppercase letter")
    if not any(ch.islower() for ch in password):
        missing.append("a lowercase letter")
    if not any(ch.isdigit() for ch in password):
        missing.append("a number")
    if not any(ch in string.punctuation for ch in password):
        missing.append("a special character")

    score = 5 - len(missing)
    if score == 5:
        rating = "Strong"
    elif score >= 3:
        rating = "Moderate"
    else:
        rating = "Weak"

    return rating, missing


if __name__ == "__main__":
    sample = "Python2026"
    rating, missing = check_password_strength(sample)
    print(f"Password: {sample} -> {rating}")
    if missing:
        print("Missing:", ", ".join(missing))