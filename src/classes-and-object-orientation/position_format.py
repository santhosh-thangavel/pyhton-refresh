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
        # return (
        #     f"{abs(self.latitude)}° {self.latitude_hemisphere},"
        #     f" {abs(self.longitude)}°{self.longitude_hemisphere}"
        # )
        return format(self)

    def __format__(self, format_spec):
        component_format_spec = ".2f"
        prefix, dot, suffix = format_spec.partition(".")
        if dot:
            num_decimal_places = int(suffix)
            component_format_spec = f".{num_decimal_places}f"
        latitude = format(abs(self.latitude), component_format_spec)
        longitude = format(abs(self.longitude), component_format_spec)
        return (
            f"{latitude}° {self.latitude_hemisphere},"
            f" {longitude}°{self.longitude_hemisphere}"
        )


class EarthPosition(Position):
    pass


class MarsPosition(Position):
    pass


mars_mountain = MarsPosition(20.459869, 36.234765)
print(
    format(mars_mountain)
)  # The built in format function passes an empty string which is handled by our function as".2f
print(format(mars_mountain, ".0"))
print(format(mars_mountain, ".1"))
print(format(mars_mountain, ".4"))
print(mars_mountain)
print(f"the mars mountain is at {mars_mountain:.5}")
print(f"{mars_mountain=}")  # dunder repr result aimed at developers
print(
    str(mars_mountain)
)  # is same as print(mars_mountain) in line 89 and hence line 55 to 58 is replaced line 59
