import iso6346


class ShippingContainer:

    next_serial = 1337
    HEIGHT_FT = 8.5
    WIDTH_FT = 8

    # When we invoke ShippingContainer._generate_serial the ShippingContainer class object is passed as the cls
    # argument of the class method which we then refer to within body of the method to locate the next serial class attribute

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6))

    @classmethod
    def create_empty(cls, owner_code, length_ft, **kwargs):
        return cls(owner_code, length_ft, contents=[], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, **kwargs):
        return cls(owner_code, length_ft, contents=list(items), **kwargs)

    @property
    def volume_of_container(self):
        return self._calc_volume()

    def _calc_volume(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft

    def __init__(self, owner_code: str, length_ft, contents: [str], **kwargs):
        self.owner_code = owner_code
        self.contents = contents
        self.length_ft = length_ft
        self.bic = self._make_bic_code(  # For a polymorphic dispatch, invoke static methods through self
            owner_code=owner_code,  # self._make_bic_code() instead ShippingContainer._make_bic_code()
            serial=ShippingContainer._generate_serial(),
        )


class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME = 100

    def __init__(
        self,
        owner_code: str,
        length_ft,
        contents: [str],
        *,
        temp_celsius: float,
        **kwargs
    ):
        super().__init__(owner_code, length_ft, contents, **kwargs)
        # if temp_celsius > RefrigeratedShippingContainer.MAX_CELSIUS:
        #     raise ValueError("Temperature too hot !")
        self._temperature_celsius = None
        self.temp_celsius = temp_celsius

    @staticmethod
    def _c_to_f(temp_celsius):
        return temp_celsius * 9 / 5 + 32

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    @property  # Method behaves like an attribute because of @property decorator
    def temp_celsius(self):  # Read only attribute. so attribute can't be set
        return self._temperature_celsius

    @temp_celsius.setter  # Write only attribute. attribute can be set
    def temp_celsius(self, value):  # Don't override properties directly.
        self._set_temp_celsius(
            value
        )  # Delegate to regular methods and over ride those instead like one below

    def _set_temp_celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot !")
        self._temperature_celsius = value

    @property  # properties don't need to be backed by attributes
    def fahrenheit(self):
        return RefrigeratedShippingContainer._c_to_f(self.temp_celsius)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.temp_celsius = RefrigeratedShippingContainer._f_to_c(value)

    # To override a property getter we need to redefine property in a derived class and delegate to base class via
    # super() if needed

    def _calc_volume(self):
        return (
            ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft
            - RefrigeratedShippingContainer.FRIDGE_VOLUME
        )
        # return super()._calc_volume - RefrigeratedShippingContainer.FRIDGE_VOLUME

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code, serial=str(serial).zfill(6), category="R"
        )


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):

    MIN_CELSIUS = -20

    # @RefrigeratedShippingContainer.temp_celsius.setter  # Write only attribute. attribute can be set
    def _set_temp_celsius(self, value):
        # if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
        #     raise ValueError("Temperature too cold")
        # RefrigeratedShippingContainer.temp_celsius.fset(self, value)

        if not (
            HeatedRefrigeratedShippingContainer.MIN_CELSIUS
            <= value
            <= RefrigeratedShippingContainer.MAX_CELSIUS
        ):
            raise ValueError("Temperature out of range")
        super()._set_temp_celsius(value)


h1 = HeatedRefrigeratedShippingContainer.create_empty(
    "TAM", length_ft=20, temp_celsius=-18
)
print(h1.temp_celsius)
h1.temp_celsius = 4
# h1.fahrenheit = -100
# print(h1.temp_celsius)
# print(h1.volume_of_container)


# r1 = RefrigeratedShippingContainer.create_with_items("MAE", ["fish"], temp_celsius = -18)
# print(r1._temp_celsius)
# print(r1.bic)
# print(r1.owner_code)
# print(r1.contents)
# r1.ref_temp = 12
# print(r1._temp_celsius)

# r2 = RefrigeratedShippingContainer.create_empty("REC", 20, temp_celsius = -5)
# print(r2.temp_celsius)
# print(r2.fahrenheit)
# print(r2.volume_of_container)
# r2.temp_celsius = -21
# print(r2.temp_celsius)


# r2.fahrenheit = -20
# print(r2.temp_celsius)
# r3 = RefrigeratedShippingContainer.create_empty("WEL", temp_celsius = 25)


# results
# -10
# 14.0
# -28.88888888888889
# Traceback (most recent call last):
#   File "/Users/santhoshthangavel/python-refresh/src/classes-and-object-orientation/shipping_classmethod.py", line 99, in <module>
#     r3 = RefrigeratedShippingContainer.create_empty("WEL", temp_celsius = 25)
#   File "/Users/santhoshthangavel/python-refresh/src/classes-and-object-orientation/shipping_classmethod.py", line 25, in create_empty
#     return cls(owner_code, contents=[], **kwargs)
#   File "/Users/santhoshthangavel/python-refresh/src/classes-and-object-orientation/shipping_classmethod.py", line 46, in __init__
#     raise ValueError("Temperature too hot !")
# ValueError: Temperature too hot !
