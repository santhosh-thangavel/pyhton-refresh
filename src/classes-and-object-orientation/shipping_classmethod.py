class ShippingContainer:

    next_serial = 1337

    # When we invoke ShippingContainer._generate_serial the ShippingContainer class object is passed as the cls
    # argument of the class method which we then refer to within body of the method to locate the next serial class attribute

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents = [])

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()



c1 = ShippingContainer("HERM", ["Books"])
print(c1.owner_code)
print(c1.contents)
print(c1.serial)


c3 = ShippingContainer.create_empty("Mind bending")
print(c3.owner_code)
print(c3.contents)

c4 = ShippingContainer.create_with_items("Burkina", ["electronics", "lights", "Speakers"])
print(c4.contents)


c2 = ShippingContainer("Pipper", ["Alpha"])
print(c2.owner_code)
print(c2.contents)
print(c2.serial ) # or c2.next_serial or ShippingContainer.next_serial but not ShippingContainer.serial

# results
# HERM
# ['Books']
# 1337
# Mind bending
# []
# ['electronics', 'lights', 'Speakers']
# Pipper
# ['Alpha']
# 1340