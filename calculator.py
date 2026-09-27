import random

class Color:
    HEADER = "\033[95m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

history = []
last_result = None

OPERATION_ALIASES = {
    "1": "1", "+": "1",
    "2": "2", "-": "2",
    "3": "3", "*": "3", "x": "3", "X": "3",
    "4": "4", "/": "4",
}

MILESTONE_LINES = [
    "5 calculations down — you're on a roll!",
    "10 calculations! The calculator salutes you.",
    "That's a lot of math. Respect.",
]

BANNER = r"""
   _____      _            _       _             __  __           _
  / ____|    | |          | |     | |           |  \/  |         | |
 | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ | \  / | __ _ ___| |_ ___ _ __
 | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|| |\/| |/ _` / __| __/ _ \ '__|
 | |___| (_| | | (__| |_| | | (_| | || (_) | |   | |  | | (_| \__ \ ||  __/ |
  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   |_|  |_|\__,_|___/\__\___|_|
"""

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
    print(Color.YELLOW + "│ " + Color.RESET + "1 / +  Add" + " " * 19 + Color.YELLOW + "│" + Color.RESET)
    print(Color.YELLOW + "│ " + Color.RESET + "2 / -  Subtract" + " " * 14 + Color.YELLOW + "│" + Color.RESET)
    print(Color.YELLOW + "│ " + Color.RESET + "3 / *  Multiply" + " " * 14 + Color.YELLOW + "│" + Color.RESET)
    print(Color.YELLOW + "│ " + Color.RESET + "4 / /  Divide" + " " * 16 + Color.YELLOW + "│" + Color.RESET)
    print(Color.YELLOW + "│ " + Color.RESET + "5.     View history" + " " * 10 + Color.YELLOW + "│" + Color.RESET)
    print(Color.YELLOW + "│ " + Color.RESET + "6.     Clear history" + " " * 9 + Color.YELLOW + "│" + Color.RESET)
    print(Color.YELLOW + "│ " + Color.RESET + "0.     Exit" + " " * 18 + Color.YELLOW + "│" + Color.RESET)
    print(Color.YELLOW + "└──────────────────────────────┘" + Color.RESET)


def get_number(prompt):
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
        print(Color.RED + "Error: cannot divide by zero." + Color.RESET)
        return None
    return round(a / b, 4)


def show_history():
    if not history:
        print(Color.CYAN + "No calculations yet this session." + Color.RESET)
        return
    print(Color.BOLD + "Session history:" + Color.RESET)
    for i, entry in enumerate(history, 1):
        print(f"  {i}. {entry}")


def run():
    global last_result
    print_banner()
    while True:
        print_menu()
        raw_choice = input(Color.BOLD + "Choose an option: " + Color.RESET).strip()
        choice = OPERATION_ALIASES.get(raw_choice, raw_choice)

        if choice == "0":
            print(Color.CYAN + "Thanks for calculating. Goodbye!" + Color.RESET)
            break

        elif choice in ("1", "2", "3", "4"):
            first_prompt = "Enter first number (or M for last result): "
            a_raw = input(Color.RESET + first_prompt).strip()
            if a_raw.upper() == "M" and last_result is not None:
                a = last_result
                print(Color.CYAN + f"Using last result: {a}" + Color.RESET)
            else:
                while True:
                    try:
                        a = float(a_raw)
                        break
                    except ValueError:
                        print(Color.RED + random.choice(ERROR_LINES) + Color.RESET)
                        a_raw = input(first_prompt).strip()

            b_prompt = "Enter second number (or M for last result): "
            b_raw = input(b_prompt).strip()
            if b_raw.upper() == "M" and last_result is not None:
                b = last_result
                print(Color.CYAN + f"Using last result: {b}" + Color.RESET)
            else:
                while True:
                    try:
                        b = float(b_raw)
                        break
                    except ValueError:
                        print(Color.RED + random.choice(ERROR_LINES) + Color.RESET)
                        b_raw = input(b_prompt).strip()

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
                print(Color.RED + "That operation couldn't be completed." + Color.RESET)
            else:
                print(Color.GREEN + f"{random.choice(SUCCESS_LINES)} {a} {op_symbol} {b} = {result}" + Color.RESET)
                history.append(f"{a} {op_symbol} {b} = {result}")
                last_result = result
                if len(history) in (5, 10, 25, 50):
                    print(Color.BOLD + Color.YELLOW + random.choice(MILESTONE_LINES) + Color.RESET)

        elif choice == "5":
            show_history()

        elif choice == "6":
            history.clear()
            print(Color.CYAN + "History cleared." + Color.RESET)

        else:
            print(Color.RED + "That's not a valid menu option. Try again." + Color.RESET)

        print()


if __name__ == "__main__":
    run()