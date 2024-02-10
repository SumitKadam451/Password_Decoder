from urllib.request import hashlib
import colorama
from colorama import Fore,Style

# Adding color for better aesthetics.
colorama.init()
print(Fore.GREEN + Style.BRIGHT)
print()
print(r" _______     _________ _    _  ____  _   _         ")
print(r"|  __ \ \   / /__   __| |  | |/ __ \| \ | |        ")
print(r"| |__| \ \_/ /   | |  | |__| | |  | |  \| |        ")
print(r"|  ___/ \   /    | |  |  __  | |  | | . ` |        ") 
print(r"| |      | |     | |  | |  | | |__| | |\  |        ")
print(r"|_|      |_|     |_|  |_|  |_|\____/|_| \_|        ")
print(r"                                                   ")
print(r"                                                   ")
print(r" _____  ______ _____ ____  _____  ______ _____     ")
print(r"|  __ \|  ____/ ____/ __ \|  __ \|  ____|  __ \    ")
print(r"| |  | | |__ | |   | |  | | |  | | |__  | |__) |   ")   
print(r"| |  | |  __|| |   | |  | | |  | |  __| |  _  /    ")
print(r"| |__| | |___| |___| |__| | |__| | |____| | \ \    ")
print(r"|_____/|______\_____\____/|_____/|______|_|  \_\   ")
print(r"                                                   ")
print()


while True:
    # Prompting the user to select the type of hash to decode (Select 3 to quit the script).
    print()
    print ("Enter Type of Hash to be Decode (Select 3 to quit the script)!\n 1. SHA1 Hash \n 2. MD5 Hash \n 3. Quit Script")
    print() 
    k = input(">")

    if (k=="1"):
        passFound = False

        # Asking the user to input the SHA1 hash to crack.
        sha1hash = input("Please input the SH1 hash to crack.\n>")

        # Opening a file containing password guesses.
        with open ("CommanPassWords.text","r") as file:


            # Iterating through each password guess.
            for guess in file:

                # Hashing the password guess.
                hashedGuess = hashlib.sha1(bytes(guess.strip(), 'utf-8')).hexdigest()

                # Comparing the hashed guess with the provided hash.
                if hashedGuess.upper() == sha1hash.upper():

                    # If a match is found, printing the password guess and exiting.
                    print("The password is ", str(guess))
                    passFound=True
                    break
                elif hashedGuess != sha1hash:

                    # If no match is found, indicating that and trying the next guess.
                    print("Password guess ",str(guess)," does not match, trying next...")

        # Indicating if no match was found after all guesses.
        if (passFound==False):
            print("Password not in database, we'll get them next time.")

    elif (k=="2"):
        passFound = False

        # Asking the user to input the MD5 hash to crack.
        md5hash = input("Please input the MD5 hash to crack.\n>")


        # Opening a file containing password guesses.
        with open ("CommanPassWords.text","r") as file:


        # Opening a file containing password guesses.
            for guess in file:

                # Hashing the password guess.
                hashedGuess = hashlib.md5(bytes(guess.strip(), 'utf-8')).hexdigest()

                # Comparing the hashed guess with the provided hash.
                if hashedGuess.upper() == md5hash.upper():


                    # If no match is found, indicating that and trying the next guess.
                    print("The password is ", str(guess))
                    passFound=True
                    break
                elif hashedGuess != md5hash:
                    print("Password guess ",str(guess)," does not match, trying next...")

        # Indicating if no match was found after all guesses.
        if (passFound==False):
            print("Password not in database, we'll get them next time.")

    elif (k=="3"):
        quit()