import inspect
from position import *


def auto_repr(cls):
    print(f"Decorating {cls.__name__} with auto_repr")
    members = vars(cls)
    # for name, member in members.items():
    #     print(name, member)

    if "__repr__" in members:
        raise TypeError(f"{cls.__name__} already defines __repr__")
    if "__init__" not in members:
        raise TypeError(f"{cls.__name__} does not override __init__")

    sig = inspect.signature(cls.__init__)
    parameter_names = list(sig.parameters)[1:]
    # print("__init__ parameter names:", parameter_names)

    if not all(
        isinstance(members.get(name, None), property) for name in parameter_names
    ):
        raise TypeError(
            f"Cannot apply auto_repr to {cls.__name__} because not all "
            f"__init__ parameters have matching properties "
        )

    def synthesized_repr(self):
        return "{typename}({args})".format(
            typename=type(self).__name__,
            args=", ".join(
                "{name}={value}".format(name=name, value=getattr(self, name))
                for name in parameter_names
            ),
        )

    setattr(cls, "__repr__", synthesized_repr)

    return cls


@auto_repr
class Location:
    def __init__(self, name, position):
        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    # def __repr__(self):       Line 5 - 42 @auto_repr does the same work
    #     return f"{type(self).__name__}(name = {self.name}, position = {self.position})"

    #
    # def __str__(self):
    #     return f"{self.name}"


hong_kong = Location("Hong Kong", EarthPosition(22.29, 114.16))
# stockholm = Location("Stockholm", EarthPosition(43.22, 26.7))
# cape_town = Location("Cape Town", EarthPosition(-33.93, 18.42))
# rotterdam = Location("Rotterdam", EarthPosition(51.96, 4.47))
# maracaibo = Location("Maracaibo", EarthPosition(10.65, -71.65))

# hong_kong
# print(hong_kong.__repr__())
# print(hong_kong.name)
# print(hong_kong.position)
print(hong_kong)
