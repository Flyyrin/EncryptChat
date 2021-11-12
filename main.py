from encrypt import encrypt
from decrypt import decrypt

print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("                                   _       _           _   ")
print("                                  | |     | |         | |  ")
print("   ___ _ __   ___ _ __ _   _ _ __ | |_ ___| |__   __ _| |_ ")
print("  / _ \ '_ \ / __| '__| | | | '_ \| __/ __| '_ \ / _` | __|")
print(" |  __/ | | | (__| |  | |_| | |_) | || (__| | | | (_| | |_ ")
print("  \___|_| |_|\___|_|   \__, | .__/ \__\___|_| |_|\__,_|\__|")
print("                        __/ | |                            ")
print("                       |___/|_|                            ")
print("-----------------------------------------------------------")
print("Press E to Encrypt a message")
print("Press D to Decrypt a message")
print("-----------------------------------------------------------")
choise = input("Enter a option: ")
message = input("Enter a message: ")
pwd = input("Enter a password: ")
print("-----------------------------------------------------------")

if choise is "E":
    en_message = encrypt(message)
    print("Encrypted message: "+ str(en_message) )
elif choise is "D": 
    de_message = decrypt(message)
    print("Encrypted message: "  + str(de_message) )
else:
    print("Enter a valid option.")    

