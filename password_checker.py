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





