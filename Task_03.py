import string

def check_password_strength(password):
    # Define criteria
    min_length = 8  # Minimum length requirement
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    # Calculate strength score based on criteria
    strength_score = 0
    if len(password) >= min_length:
        strength_score += 1
    if has_uppercase:
        strength_score += 1
    if has_lowercase:
        strength_score += 1
    if has_digit:
        strength_score += 1
    if has_special:
        strength_score += 1

    # Provide feedback based on score
    if strength_score == 5:
        return "Very Strong"
    elif strength_score == 4:
        return "Strong"
    elif strength_score == 3:
        return "Moderate"
    elif strength_score == 2:
        return "Weak"
    else:
        return "Very Weak"

def main():
    while True:
        password = input("Enter a password to check its strength: ")
        if password.strip() == "":
            print("Password cannot be empty. Please enter a valid password.")
            continue
        
        strength = check_password_strength(password)
        print(f"Password strength: {strength}")

        cont = input("Do you want to check another password? (yes/no): ")
        if cont.lower() != "yes":
            break

    print("Password strength checker terminated.")

if __name__ == "__main__":
    main()
