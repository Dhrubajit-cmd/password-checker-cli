import random  # For generating random numbers 
import os # To clear the screen 
import string # Provides the predefined character sets 
import getpass # Allows the user to enter the password without visible in the screen 
import math # Used to calculate password entropy for strength evaluation 

MIN_LENGTH = 8

def calculate_entropy(password): 
    """Calculates the entropy based on the character diversity and size"""
    charset_size = 0
    if any(c in string.ascii_lowercase for c in password): 
        charset_size += 26 
    if any(c in string.ascii_uppercase for c in password): 
        charset_size +=26
    if any(c in string.digits for c in password): 
        charset_size += 10 
    if any(c in string.punctuation for c in password): 
        charset_size += len(string.punctuation)
    if any(c.isspace() for c in password): 
        charset_size += 1 

    return len(password) * math.log2(charset_size) if charset_size else 0


def check_password_strength(): 
    password = getpass.getpass('Enter your password: ')
    
    if len(password) < MIN_LENGTH : 
        print(f"Your password is too short ! The minimum password length must be {MIN_LENGTH}\n")
        return 
    
    entropy = calculate_entropy(password) 
    
    lower_count = sum(1 for c in password if c in string.ascii_lowercase)
    upper_count = sum(1 for c in password if c in string.ascii_uppercase)
    num_count = sum(1 for c in password if c in string.ascii_digits)
    punc_count = sum(1 for c in password if c in string.punctuation)
    space_count = sum(1 for c in password if c.isspace())


    # Classifying password strength : 
    if entropy < 26 : 
        remarks = "Very weak password. Change it immediately"
    elif entropy < 36:
        remarks = "Weak: Can be cracked quickly. Use a stronger password."
    elif entropy < 60:
        remarks = "Moderate: Decent password, but can still be improved."
    elif entropy < 80:
        remarks = "Strong: Hard to guess, but consider making it longer."
    else:
        remarks = "Very Strong: Excellent password! Highly secure."

   
    # Display password analysis : 

    print (f"\nPassoword analysis for {password}")
    print(f"🔹 {lower_count} lowercase letters")
    print(f"🔹 {upper_count} uppercase letters")
    print(f"🔹 {num_count} digits")
    print(f"🔹 {punc_count} special characters")
    print(f"🔹 {space_count} whitespace characters")
    print(f"🔹 Entropy Score: {entropy:.2f} bits")
    print(f"🔹 Remarks: {remarks}\n")

def check_another_password(): 
    """Asks if the user wants to check another password"""
    while True: 
        choice = input(" 🔄 Do you want to check another password ? (y/n): ").strip().lower()

        if choice == 'y': 
            return True 
        elif choice == 'n': 
            print("👋 Exiting... Stay secure!")
            return False
        else: 
            print("⚠️ Invalid input. Please enter 'y' or 'n'.")