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

    @property
    def latitude_hemisphere(self):
        return "N" if self.latitude >= 0 else "S"

    @property
    def longitude_hemisphere(self):
        return "E" if 180 > self.longitude >= 0 else "W"

    # def __repr__(self):
    #     return f"Position(latitude = {self.latitude}, longitude = {self.longitude})"

    # Currently we have type of self (which is "position" in this case) is hard coded.
    # Perfectly fine as long as there are no inheritance and subclasses.
    # In case of inheritance self may be some subclass so we need to get actual run time type of self
    # how do we do it is as below

    def __repr__(self):
        # return f"{self.__class__.__name__}(latitude = {self.latitude}, longitude = {self.longitude})"
        return f"{type(self).__name__}(latitude = {self.latitude}, longitude = {self.longitude})"

    # ------------------------------------------repr-------------------------------------------------------
    # type of returned string is ideally formatted as a source code for a constructor call
    # class of an object is same as type of an object which is
    # return return f"{type(self).__name__}(latitude = {self.latitude}, longitude = {self.longitude})"
    # but this builtin function won't work to get the name of a class

    # def typename(obj):
    #     return type(obj).__name__

    # will get the Type of the obj and then its class using __name__
    # return f"{typename(self)}(latitude = {self.latitude}, longitude = {self.longitude})"
    # the above line is expected to work but it doesn't
    # ----------------------------------------------------------------------------------------------------------

    def __str__(self):
        return (
            f"{abs(self.latitude)}° {self.latitude_hemisphere},"
            f" {abs(self.longitude)}°{self.longitude_hemisphere}"
        )


class EarthPosition(Position):
    pass


class MarsPosition(Position):
    pass


mars_mountain = MarsPosition(20, 36)

# repr representation
print(repr(mars_mountain))
# str representation
print(str(mars_mountain))
print("mars mountain is located at", mars_mountain)
# format representation
print(format(mars_mountain))  # It takes the str representation

# Results
# MarsPosition(latitude = 20, longitude = 36)
# 20° N, 36°E
# mars mountain is located at 20° N, 36°E
# 20° N, 36°E
