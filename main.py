from utils.miles_util import MilesUtil
from utility import Utility
import menu_handler

utilities = [
    MilesUtil()
]


def main():
    target_util: Utility = menu_handler.show_and_input_menu(utilities)
    target_util.run()


main()
