import yaml

from utils.default.number_util import NumberUtil
from utils.menu import menu_handler
from utils.utility import Utility

utilities = []


def main():

    load_utilities()

    target_util: Utility = menu_handler.show_and_input_menu(utilities)
    result: str = target_util.run()

    Utility.print_formatted(result)


def load_utilities():
    with open('converters.yaml', 'r') as file:
        converter = yaml.safe_load(file)

        for key, rows in converter.items():
            # Check each row type

            if isinstance(rows, dict):
                utilities.append(NumberUtil(key, rows['from'], rows['to'], float(rows['multiplier'])))
            else:
                print("Error: Row is not a dictionary")


main()
