import random
import string

def generate_password(length, complexity):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = []

    # Ensure required numbers, special characters, and uppercase letters
    while len(password) < length:
        char = random.choice(characters)
        if complexity == 1:
            if char.islower() or char.isupper():
                password.append(char)
        elif complexity == 2:
            if char.islower() or char.isupper() or char.isdigit():
                password.append(char)
        elif complexity == 3:
            password.append(char)
    
    # Shuffle to avoid patterns
    random.shuffle(password)
    
    return ''.join(password)

def generate_weak_password():
    return generate_password(length=8, complexity=1)

def generate_standard_password():
    return generate_password(length=12, complexity=2)

def generate_strong_password():
    return generate_password(length=16, complexity=3)

