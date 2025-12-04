import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    # Number check
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Add at least one number (0-9).")

    # Special character check
    if re.search(r"[!@#$%^&*()_+=\-{};:'\",.<>?/\\|`~]", password):
        strength += 1
    else:
        feedback.append("Add at least one special character.")

    # Final strength score
    if strength == 5:
        return "Strong password 💪", []
    elif strength >= 3:
        return "Medium password ⚠️", feedback
    else:
        return "Weak password ❌", feedback


if __name__ == "__main__":
    pwd = input("Enter your password: ")
    status, tips = check_password_strength(pwd)

    print("\nPassword Status:", status)
    if tips:
        print("\nSuggestions to improve:")
        for t in tips:
            print("- " + t)

