# password_generator.py
import random
import string

def generate_password(length=12, lower=True, upper=True, digits=True, symbols=True):
    pool = ''
    if lower: 
        pool += string.ascii_lowercase
    if upper: 
        pool += string.ascii_uppercase
    if digits: 
        pool += string.digits
    if symbols: 
        pool += string.punctuation
    if not pool:
        raise ValueError("No character types selected")
    return ''.join(random.choice(pool) for _ in range(length))

def main():
    try:
        length_input = raw_input("Password length (8-24) [12]: ").strip()  # raw_input for Python 2
        length = int(length_input) if length_input else 12

        if length < 8 or length > 24:
            raise ValueError("Password length must be between 8 and 24")

        pwd = generate_password(length=length)
        print "\nGenerated password:\n", pwd   # print statement in Python 2

    except Exception as e:
        print "Error:", e

if __name__ == "__main__":
    main()
