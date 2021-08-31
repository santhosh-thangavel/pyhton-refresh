class SimpleList:
    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"{type(self).__name__}({self._items!r})"


class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()


class IntList(SimpleList):
    def __init__(self, items=()):
        for x in items:
            self._validate(x)
            s = super()
            print(s)
            s.__init__(items)
            print(s.__init__)
        # super().__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError("IntList supports only integer values")

    def add(self, item):
        self._validate(item)
        super().add(item)


class SortedIntList(IntList, SortedList):
    pass


sil = SortedIntList([23, 3, 16])
print(sil)
sil.add(96)
print(sil)  # Sorted because MRO contains IntList and SortedList
# SortedIntList([2, 45, 3, "67"])
print(SortedIntList.__bases__)
print(SortedIntList.__mro__)
print(sil)

# il = IntList([3, 5, 7, 1, 9])
# il.add(6)
# print(il)
# il.add("23")

# sl = SortedList([23, 44, 1, 19, 76])
# print(sl)
# print(len(sl))
# sl.add(67)
# print(sl)
