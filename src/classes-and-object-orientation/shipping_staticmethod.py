class ShippingContainer:

    next_serial = 1337

    @staticmethod
    def _generate_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()




c1 = ShippingContainer("HERM", ["Books"])
print(c1.owner_code)
print(c1.contents)
print(c1.serial)

c2 = ShippingContainer("Pipper", ["Alpha"])
print(c2.owner_code)
print(c2.contents)
print(c2.serial ) # or c2.next_serial or ShippingContainer.next_serial but not ShippingContainer.serial
