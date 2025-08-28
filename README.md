PIN CRACKING TOOL

How It Works:

1. User Input:
Prompts the user to enter a SHA-256 hashed PIN (in hexadecimal).

2. Brute-Force Attack Loop:
Starts trying PINs from length 1 upwards (e.g., 0, 1, ..., 9, then 00, 01, ..., 99, and so on).
For each guess, it:
Hashes the guessed PIN using hashlib.sha256().
Compares it to the provided hash.
Logs and prints each attempt to the terminal (including the current PIN and its SHA-256 hash).

3. Success Logging:
Once a match is found:
Prints a success message.
Saves the cracked hash, its corresponding PIN, and timestamp into a file named RekPins.log.
