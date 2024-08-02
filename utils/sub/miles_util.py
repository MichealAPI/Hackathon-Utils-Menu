from utils.default.number_util import NumberUtil


class MilesUtil(NumberUtil):

    def __init__(self):
        super().__init__("Miles", "Kilometres", 1.60934)

    def get_description(self) -> str:
        return "MilesUtil - Convert your Miles into Kilometres"

    def print_source(self):
        print("You're using an Utility from MilesUtil")

    def get_arg_description(self, at: int) -> None:
        return {
            0: "Insert your amount of Miles:"
        }.get(at)
