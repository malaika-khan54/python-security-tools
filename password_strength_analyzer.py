import re

def analyze_password(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Use at least 12 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback


print("Password Strength Analyzer")
print("-" * 30)

password = input("Enter a password to evaluate: ")

strength, feedback = analyze_password(password)

print(f"\nPassword strength: {strength}")

if feedback:
    print("\nSuggestions to improve your password:")
    for item in feedback:
        print(f"- {item}")
else:
    print("\nGreat job. Your password meets all recommended requirements.")
    
input("\nPress Enter to exit...")
