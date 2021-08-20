"""Model for aircraft flights"""


class Flight:



    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")

        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code in '{number}'")

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{number}'")

        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):
        print(self._aircraft.model())

    def number(self):
        print(self._number)

    def airline(self):
        print(self._number[:2])

class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        print(self._registration)

    def model(self):
        print(self._model)

    def seating_plan(self):
        return range(1, self._num_rows), "ABCDEFGHJK"[:self._num_seats_per_row]  # understand it properly

f = Flight("SN060", Aircraft("EU-PAT", "Boeing999", num_rows=22, num_seats_per_row=6))
f.number()
# a = Aircraft("EU-PAT", "Boeing999", num_rows=22, num_seats_per_row=6)

# f.registration()
f.aircraft_model()
# f.seating_plan()