def sequence_class(immutable):
    if immutable:
        cls = tuple
    else:
        cls = list
    print(cls)


sequence_class("Nairobi")


# class object

# You can achieve the same results using conditional expressions

def sequence_class_condition_exp(immutable):
    return tuple if immutable else list


seq = sequence_class_condition_exp(immutable=False)
s = seq("Nairobi")
print(s)
print(type(s))
