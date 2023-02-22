class Utils:

    @staticmethod
    def flatten(list):
        return [item for nested_list in list for item in nested_list]


class PrintUtils(Utils):

    @staticmethod
    def print_rjust(message, fill=' ', adjust_amount=20):
        print(message.rjust(adjust_amount, fill))
