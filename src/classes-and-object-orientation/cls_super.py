class Animal:
    @classmethod
    def description(cls):
        return "An animal"


class Bird(Animal):
    @classmethod
    def description(cls):
        s = super()
        print(s)
        return s.description() + "with wings"
        # return super().description() + " with wings"


class Flamingo(Bird):
    @classmethod
    def description(cls):
        return super().description() + " pink in color"


print(Animal.description())
print(Bird.description())
print(Flamingo.description())
