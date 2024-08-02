from utils.utility import Utility


class NumberUtil(Utility):

    def __init__(self, identifier: str, from_type: str, to_type: str, multiplier: float):
        self.multiplier = multiplier
        self.from_type = from_type
        self.to_type = to_type
        self.identifier = identifier

    def run(self) -> str:
        values = super().input_values()

        if not self.perform_checks(values):
            print("Some checks have gone wrong")
            return "Something went wrong, please retry again later"

        v1 = values[0]

        return f"Your {self.from_type} amount expressed in {self.to_type} is: {v1 * self.multiplier} {self.to_type.lower()}"

    def get_required_args_amount(self) -> int:
        return 1

    def get_required_type(self) -> type:
        return int

    def get_description(self) -> str:
        return f"{self.identifier} - Convert your {self.from_type} into {self.to_type}"

    def print_source(self):
        print(f"You're using an Utility from {self.identifier}")

    def perform_checks(self, list_var: list) -> bool:
        return Utility.perform_checks(self, list_var)

    def get_arg_description(self, at: int) -> None:
        return {
            0: f"Insert your amount of {self.from_type}:"
        }.get(at)
