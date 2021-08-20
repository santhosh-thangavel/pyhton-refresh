class MarkBook:

    def __init__(self):
        self.marks = {}

    def add(self, name, mark):
        self.marks[name] = mark

    def lookup(self, name):
        return self.marks[name]

    def is_consistent(self):
        for name1, mark1 in self.marks.items():
            for name2, mark2 in self.marks.items():
                if name1 == name2:
                    continue
                if mark1.startswith(mark2):
                    return False
        return True

    def get_names(self):
        return set(self.marks.keys())

    def get_numbers(self):
        return set(self.marks.values())