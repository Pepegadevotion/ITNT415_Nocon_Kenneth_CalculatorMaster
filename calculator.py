
import random

# --- ANSI colors (most terminals, including the VM's, support these) ---
class Color:
    HEADER = "\033[95m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

# Keeps a running log of calculations for this session only (not saved to disk)
history = []

BANNER = r"""
   _____      _            _       _             __  __           _
  / ____|    | |          | |     | |           |  \/  |         | |
 | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ | \  / | __ _ ___| |_ ___ _ __
 | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|| |\/| |/ _` / __| __/ _ \ '__|
 | |___| (_| | | (__| |_| | | (_| | || (_) | |   | |  | | (_| \__ \ ||  __/ |
  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   |_|  |_|\__,_|___/\__\___|_|
"""

# A little flavor text so results don't feel robotic
SUCCESS_LINES = [
    "Crunched it.",
    "Math says yes.",
    "Numbers obey.",
    "Boom, solved.",
    "Easy work.",
]

ERROR_LINES = [
    "That input tripped the calculator up.",
    "Numbers only, please — the calculator got confused.",
    "Invalid entry. Try again.",
]


def print_banner():
    print(Color.CYAN + BANNER + Color.RESET)
    print(Color.BOLD + "        Welcome to Calculator Master — pick an operation below" + Color.RESET)
    print()


def print_menu():
    print(Color.YELLOW + "┌──────────────────────────────┐" + Color.RESET)
    print(Color.YELLOW + "│ " + Color.RESET + "1. Add" + " " * 24 + Color.YELLOW + "│" + Color.RESET)
    print(Color.YELLOW + "│ " + Color.RESET + "2. Subtract" + " " * 19 + Color.YELLOW + "│" + Color.RESET)
    print(Color.YELLOW + "│ " + Color.RESET + "3. Multiply" + " " * 19 + Color.YELLOW + "│" + Color.RESET)
    print(Color.YELLOW + "│ " + Color.RESET + "4. Divide" + " " * 21 + Color.YELLOW + "│" + Color.RESET)
    print(Color.YELLOW + "│ " + Color.RESET + "5. View history" + " " * 15 + Color.YELLOW + "│" + Color.RESET)
    print(Color.YELLOW + "│ " + Color.RESET + "0. Exit" + " " * 23 + Color.YELLOW + "│" + Color.RESET)
    print(Color.YELLOW + "└──────────────────────────────┘" + Color.RESET)


def get_number(prompt):
    """
    Shared input helper: keeps asking until the user gives a valid number.
    This is here so every operation gets input validation for free —
    but you're welcome to move/rewrite this logic inside your own branch
    if you'd rather each operation handle validation itself.
    """
    while True:
        raw = input(prompt)
        try:
            return float(raw)
        except ValueError:
            print(Color.RED + random.choice(ERROR_LINES) + Color.RESET)


def add(a, b):
    return round(a + b, 4)


def subtract(a, b):
    return round(a - b, 4)


def multiply(a, b):
    return round(a * b, 4)


def divide(a, b):
    if b == 0:
        print(Color.RED + "Cannot divide by zero." + Color.RESET)
        return None
    return a / b


# ----------------------------------------------------------------------

def show_history():
    if not history:
        print(Color.CYAN + "No calculations yet this session." + Color.RESET)
        return
    print(Color.BOLD + "Session history:" + Color.RESET)
    for i, entry in enumerate(history, 1):
        print(f"  {i}. {entry}")


def run():
    print_banner()
    while True:
        print_menu()
        choice = input(Color.BOLD + "Choose an option: " + Color.RESET).strip()

        if choice == "0":
            print(Color.CYAN + "Thanks for calculating. Goodbye!" + Color.RESET)
            break

        elif choice in ("1", "2", "3", "4"):
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")

            if choice == "1":
                result = add(a, b)
                op_symbol = "+"
            elif choice == "2":
                result = subtract(a, b)
                op_symbol = "-"
            elif choice == "3":
                result = multiply(a, b)
                op_symbol = "*"
            else:
                result = divide(a, b)
                op_symbol = "/"

            if result is None:
                print(Color.RED + "This operation hasn't been implemented yet — check out its branch!" + Color.RESET)
            else:
                print(Color.GREEN + f"{random.choice(SUCCESS_LINES)} {a} {op_symbol} {b} = {result}" + Color.RESET)
                history.append(f"{a} {op_symbol} {b} = {result}")

        elif choice == "5":
            show_history()

        else:
            print(Color.RED + "That's not a valid menu option. Try again." + Color.RESET)

        print()


if __name__ == "__main__":
    run()
