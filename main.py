import string
import random
import sys


def generateRandomPassword(passwordLength):
    password = []

    for i in range(passwordLength):
        password.append(random.choice(string.digits + string.ascii_letters + string.punctuation))

    return ''.join(password)


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Please enter the length of your password that you want to create.")
    else:
        passwordLength = sys.argv[1]

        if sys.argv[1].strip().isdigit():
            length = len(passwordLength)

            print("Your password is: " + generateRandomPassword(int(passwordLength)))
        else:
            print("Please enter the length of your desired password as a number.")
