class Position:
    def __init__(self, latitude, longitude):
        self._latitude = latitude
        self._longitude = longitude

        if not (-90 <= latitude <= +90):
            raise ValueError(f"Latitude {latitude} out of range")

        if not (-180 <= longitude <= +180):
            raise ValueError(f"Longitude{longitude} out of range")

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    # def __repr__(self):
    #     return f"Position(latitude = {self.latitude}, longitude = {self.longitude})"

    # Currently we have type of self (which is "position" in this case) is hard coded.
    # Perfectly fine as long as there are no inheritance and subclasses.
    # In case of inheritance self may be some subclass so we need to get actual run time type of self
    # how do we do it is as below

    def __repr__(self):
        # return f"{self.__class__.__name__}(latitude = {self.latitude}, longitude = {self.longitude})"
        return f"{type(self).__name__}(latitude = {self.latitude}, longitude = {self.longitude})"

    # type of returned string is ideally formatted as a source code for a constructor call
    # class of an object is same as type of an object which is
    # return return f"{type(self).__name__}(latitude = {self.latitude}, longitude = {self.longitude})"
    # but this builtin function won't work to get the name of a class

    # def typename(obj):
    #     return type(obj).__name__

    # will get the Type of the obj and then its class using __name__
    # return f"{typename(self)}(latitude = {self.latitude}, longitude = {self.longitude})"
    # the above line is expected to work but it doesn't


class EarthPosition(Position):
    pass


class MarsPosition(Position):
    pass


# sydney = Position(-20, 32)
# print(repr(sydney))
# r = repr(sydney)
# print(eval(r))
# print(bool(repr(sydney) == eval(r)))  # the objects are different
#
# london = EarthPosition(70, 120)
# print(london)
# print(repr(london))
# print(eval(repr(london)))
# print(bool(repr(london) == eval(repr(london))))  # the objects are different
#
#
# mars_mountain = MarsPosition(20, 36)
# print(mars_mountain)
# print(repr(mars_mountain))
# print(eval(repr(mars_mountain)))
# print(
#     bool(repr(mars_mountain) == eval(repr(mars_mountain)))
# )  # the objects are different
#
# print(str(mars_mountain))
# print(format(mars_mountain))

# ----------------------------------------------------------------------------------------
# Results
# Position(latitude = -20, longitude = 32)
# Position(latitude = -20, longitude = 32)
# False
# EarthPosition(latitude = 70, longitude = 120)
# EarthPosition(latitude = 70, longitude = 120)
# EarthPosition(latitude = 70, longitude = 120)
# False
# MarsPosition(latitude = 20, longitude = 36)
# MarsPosition(latitude = 20, longitude = 36)
# MarsPosition(latitude = 20, longitude = 36)
# False
# MarsPosition(latitude = 20, longitude = 36)
# MarsPosition(latitude = 20, longitude = 36)
