class Utility:

    def run(self) -> str:
        pass

    def get_required_args_amount(self) -> int:
        pass

    def get_required_type(self) -> type:
        pass

    def print_source(self):
        pass

    def get_arg_description(self, at: int) -> None:
        pass

    def get_description(self) -> str:
        pass

    @staticmethod
    def perform_checks(self, list_var: list) -> bool:

        if not Utility.has_enough_args(list_var, self.get_required_args_amount()):
            print("Not enough args have been given")
            return False

        if not Utility.check_types(list_var, self.get_required_type(), self.get_required_args_amount()):
            print("Not enough correct-type args")
            return False

        return True

    # Args length checks must be performed before this checker
    @staticmethod
    def check_types(list_var: list, reference_class: type, involved_args_amount: int) -> bool:

        for index in range(involved_args_amount):

            fixed_index = index - 1

            if not isinstance(list_var[fixed_index], reference_class):
                print(f"Arg at {index} isn't of type {reference_class}")
                return False

        return True

    @staticmethod
    def has_enough_args(list_var: list, involved_args_amount: int) -> bool:
        return len(list_var) >= involved_args_amount

    def input_values(self) -> list:

        result: list = []

        my_type = self.get_required_type()

        print(f"My type: {my_type}")

        for i in range(self.get_required_args_amount()):
            val = my_type(input(self.get_arg_description(i)))
            result.append(val)

        return result
