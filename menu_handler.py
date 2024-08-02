from utility import Utility


def show_and_input_menu(utilities: list) -> Utility | None:
    for index in range(len(utilities)):
        utility = utilities[index]

        print(f"{index}. {utility.get_description()}")

    target_choice: int = int(input("Insert your utility id to begin:"))

    # check if it is in range
    if target_choice > len(utilities) or target_choice < 0:
        print("Aborting... invalid choice")
        return None

    return utilities[target_choice]
