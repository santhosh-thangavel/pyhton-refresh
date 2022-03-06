class PositiveIntegers:
    def __init__(self, positive_integer):
        # self._positive_integer = positive_integer
        self._number = positive_integer
    def integer_numbers(self):
        if self._number == int(self._number):
            sum_of_first_positive_integers = ((self._number) * (self._number + 1)) / 2
            print(f"sum of first n positive integers = {int(sum_of_first_positive_integers)}")
        else:
            print(f"Input an integer and not a float or string, please")

f = PositiveIntegers(3)
f.integer_numbers()


