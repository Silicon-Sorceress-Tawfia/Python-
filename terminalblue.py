import time
import os

def print_blue():
    os.system("cls" if os.name == "nt" else "clear")  # Clear the terminal screen (for Windows or UNIX)
    print("\033[34m" + " " * 20 + "This is Blue!" + " " * 20 + "\033[0m")
    time.sleep(2)

if __name__ == "__main__":
    while True:
        print_blue()
