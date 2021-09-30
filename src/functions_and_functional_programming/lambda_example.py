scientist = [
    "Marie Curie",
    "Albert Einstein",
    "Rosalind Franklin",
    "Niels Bohr",
    "Dian Fossey",
    "Isaac Newton",
    "Grace Hopper",
    "Charles Darwin",
    "Lise Meitner",
]

sorted_names = sorted(scientist, key=lambda name: name.split()[-1])
print(sorted_names)


# Lambda is itself an expression, which results in a callable object
# lambda argument:expression
# expression is returned so no return statement is allowed, doc strings cannot be used, nameless function
last_name = lambda name: name.split()[-1]
print(last_name)
t = last_name("Nikola Tesla")
print(t)


# Regular function
def first_name(name):
    print(name.split()[0])


first_name("Nikola Tesla")
