Project 3 - Random Password Generator
DecodeLabs Python Internship (Batch 2026)
What it does
Generates a secure, random password based on user preferences.
Asks for password length (minimum 8 characters)
Lets the user choose which character types to include:
Uppercase letters (A-Z)
Lowercase letters (a-z)
Numbers (0-9)
Symbols (@, #, $, etc.)
Guarantees at least one character from each selected type
Shows the password's entropy (strength in bits)
Key concepts used
secrets module for cryptographically secure randomness (not random)
string module for ready-made character sets
''.join() for efficient string building
Input validation with while True + try/except
How to run
python password_generator.py
Follow the prompts to set your desired length and character types.
Example output
Enter desired password length (min 8): 12
Include uppercase letters (A-Z)? (y/n): y
Include lowercase letters (a-z)? (y/n): y
Include numbers (0-9)? (y/n): y
Include symbols (@,#,$)? (y/n): y
Your secure password: v12p1?THu4]~
Entropy strength: 78.66 bits
