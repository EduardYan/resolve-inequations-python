"""
FUNCTIONS AND CLASSES TO USE IN THE PROGRAM.
"""


class Inequation:
    def __init__(self, expression:list):
        self.expression = expression

    def resolve(self):
        first_member = int(self.expression["first_member"])
        second_member = int(self.expression["second_member"])

        result = second_member / first_member
        print(f"RESULT ------ {result}")

    def show(self):
        print(f" EXPRESSION ------ {self.expression['first_member']}x {self.expression['inequation_sign']} {self.expression['second_member']}\n")


def loop():
    print(
        """
        ---- RESOLVE INEQUATIONS ----
        EXAMPLE:
        2x > 8
        """
    )

    first_member = input("FIRST MEMBER (2x) ---- : ")
    second_member = input("SECOND MEMBER (8) ---- : ")
    inequation_sign = input("INEQUATION SIGN (<,>,<=,>=) --- : ")

    expression  = {
        "first_member": first_member,
        "second_member": second_member,
        "inequation_sign": inequation_sign
    }

    return expression

