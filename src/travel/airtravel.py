"""
Model for aircraft flights
"""


class Flight:

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{number}'")
        self._number = number
        self._aircraft = aircraft

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()


class Aircraft:

    def __init__(self, registration: str, model: str, num_rows: int, num_seats_per_row: int):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row])


f = Flight("SN060", Aircraft("T-DPTG", "Airbus A380", num_rows=22, num_seats_per_row=6))
print(f.airline())
print(f.aircraft_model())

# a = Aircraft("T-DPTG", "Airbus A380", num_rows=22, num_seats_per_row=6)
#
# print(a.registration())
#
# print(a.model())
#
# print(a.seating_plan())
