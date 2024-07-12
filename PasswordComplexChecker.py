import re
print("------------- Password Strength Assessment Tool --------------")
def assess_password_strength(password):
    # Define criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Assess the password strength
    if all([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria]):
        return "Strong Password"
    elif length_criteria and (uppercase_criteria or lowercase_criteria) and digit_criteria:
        return "Moderate Password"
    elif length_criteria and (uppercase_criteria or lowercase_criteria):
        return "Weak Password"
    else:
        return "Very Weak Password"

def main():
    while True:
        print("\nEnter a password to assess its strength or type 'q' to quit:")
        password = input("Password: ")
        
        if password.lower() == 'q':
            print("Exiting the program.")
            break

        # Assess and display the password strength
        strength = assess_password_strength(password)
        print(f"Password Strength: {strength}")

if __name__ == "__main__":
    main()
