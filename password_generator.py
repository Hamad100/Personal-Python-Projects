import random

print("Welcome To Your Password Generator")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789"

numberOfPass = input("How many passwords would you like to generate today? ")
numberOfPass = int(numberOfPass)

passLength = input("Your password length: ")
passLength = int(passLength)

print("\nHere are your passwords:")

for pwd in range(numberOfPass):
    passwords = ""
    for c in range(passLength):
        passwords += random.choice(chars)
    print(passwords)
