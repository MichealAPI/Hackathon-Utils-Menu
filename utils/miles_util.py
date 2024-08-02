from utility import Utility


class MilesUtil(Utility):

    def run(self) -> str:
        values = super().input_values()

        if not self.perform_checks(values):
            print("Some checks have gone wrong")
            return "Something went wrong, please retry again later"

        v1 = values[0]

        return f"Your miles amount expressed in kilometers is: {v1 * 1.60934}km"

    def get_required_args_amount(self) -> int:
        return 1

    def get_required_type(self) -> type:
        return int

    def get_description(self) -> str:
        return "MilesUtil - Convert your Miles into Kilometres"

    def print_source(self):
        print("You're using an Utility from MilesUtil")

    def perform_checks(self, list_var: list) -> bool:
        return Utility.perform_checks(self, list_var)

    def get_arg_description(self, at: int) -> None:
        return {
            0: "Insert your amount of Miles:"
        }.get(at)
