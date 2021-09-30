def sequence_class(immutable):
    if immutable:
        cls = tuple
    else:
        cls = list
    print(cls)


sequence_class("Nairobi")

# class object
