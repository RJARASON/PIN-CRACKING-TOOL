import hashlib
import os
import pattern
from datetime import datetime
import time
try:
    nowdt=datetime.now()
    currentdate=nowdt.strftime("%Y-%m-%d")
    currenttime=nowdt.strftime("%H: %M %p: %S")
    def generate_all_pins(length):
        for i in range(10 ** length):
            yield str(i).zfill(length)
    os.system("cls" if os.name == "nt" else "clear")
    pattern.patterntitle()
    print("\033[91m\nImportant Notice!\033[0m\nThis software script constitutes a brute-force hashing utility capable of conducting exhaustive cryptographic operations to ascertain the original plaintext (PIN) from its corresponding SHA-256 hash. It is imperative to understand that the deployment of this utility in any context outside of explicitly authorized, ethical, or legally sanctioned environments constitutes a potential criminal offense and is unequivocally prohibited.\n")
    print("\033[0m="*80)
    hashedpin = input("\033[96mEnter Hashed PIN (SHA-256 Only!):\033[0m ").strip().lower()
    attempts = 0
    length = 1
    print("\n[!] NOTE : Hashed pins may take a very long time to guess depending on the length.")
    print("Please wait...")
    time.sleep(5)
    print("\033[94mexecuting...")
    time.sleep(2)
    while True:
        print(f"\033[0m\nTrying PINs with length {length}...")
        for guess in generate_all_pins(length):
            attempts += 1
            targethash = hashlib.sha256(guess.encode()).hexdigest()
            print(f"\033[92m|Trying > [{guess}] >>> [{targethash}]\033[0m")
            if targethash == hashedpin:
                file=open("RekPins.log",'a')
                print("\033[93m="*80)
                file.write(f"\n{targethash} >>> {guess}\nExecuted on :  {currentdate}  |  {currenttime}\n")
                print("\033[93m\n[+] PIN found")
                print("\033[93m[+] Stored in : RekPins.log")
                print(f"\033[93m[+] Total Attempts: {attempts} attempts\033[0m")
                exit()
        length += 1 

except (Exception,KeyboardInterrupt):
    print("\n\n\033[91m[!] An unexpected error occured or system got interrupted.\033[0m")
    exit()