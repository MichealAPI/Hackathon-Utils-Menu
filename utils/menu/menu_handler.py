from utils.utility import Utility


def show_and_input_menu(utilities: list) -> Utility | None:

    print_header()

    for index in range(len(utilities)):
        utility = utilities[index]

        print(f"{index}. {utility.get_description()}")

    print_footer()

    target_choice: int = int(input("\nInsert your utility id to begin:\n"))

    # check if it is in range
    if target_choice > len(utilities) or target_choice < 0:
        print("Aborting... invalid choice")
        return None

    return utilities[target_choice]


def print_header():
    print("_-======= Menu =======-_")


def print_footer():
    print("-_==== Hackathon! ====_-")
