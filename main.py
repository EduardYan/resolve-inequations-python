"""
THIS IS A SMALL PROGRAM FOR
RESOLVE INECUATIONS.


"""

from helpers.funcs import Inequation, loop


if __name__ == '__main__':

    print(" WELCOME !!! \n")

    while True:
        expression = loop()
        inequation = Inequation(expression)

        inequation.show()
        inequation.resolve()
