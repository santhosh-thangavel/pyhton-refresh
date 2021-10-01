def start_up_name(args1, **kwargs):
    print(args1)
    print(kwargs)
    # print(type(kwargs))


start_up_name(args1="new", industry="IT", location="London", employee=10)

# Result
# new
# {'industry': 'IT', 'location': 'London', 'employee': 10}

# positional argument cannot follow keyword argument
# def not_allowed(**kwargs, *args):
#     print(args)
#     print(kwargs)

# Result
# def not_allowed(**kwargs, *args):
#                             ^
# SyntaxError: invalid
# syntax


def print_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)


print_args(1, 2, 3, 4, 5)

# Result
# 1
# 2
# (3, 4, 5)


def print_args(arg1, arg2, *args, kwarg1, kwarg2):
    print(arg1)
    print(arg2)
    print(args)
    print(kwarg1)
    print(kwarg2)


print_args(1, 2, 3, 4, 5, kwarg1=6, kwarg2=7)


# result
# 1
# 2
# (3, 4, 5)
# 6
# 7
# print_args(1, 2, 3, 4, 5, 6, 7)

# Result
# print_args(1, 2, 3, 4, 5, 6, 7)
# TypeError: print_args() missing 2 required keyword-only arguments: 'kwarg1' and 'kwarg2'


# Important
# Use mandatory keyword arguments without accepting arbitrary number of positional arguments
# only key word argument after * but arbitrary number of positional argument is not allowed before *
def avoid_arbitrary_positional_argument(first_name, last_name, *, title=""):
    print(title, first_name, last_name)


avoid_arbitrary_positional_argument("king", "Alexander", title="The great")
# result
# The great king Alexander
# avoid_arbitrary_positional_argument("king", "Alexander", "II", title="The great")
# avoid_arbitrary_positional_argument("king", "Alexander", "II", title="The great") TypeError:
# avoid_arbitrary_positional_argument() takes 2 positional arguments but 3 positional arguments (and 1 keyword-only
# argument) were given


def print_args(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
    print(arg1)
    print(arg2)
    print(args)
    print(kwarg1)
    print(kwarg2)
    print(kwargs)


print_args(1, 2, 3, 4, 5, kwarg1=6, kwarg2=7, kwarg3=8, kwarg4=9)


# def print_args(arg1, arg2, *args, kwarg1, kwarg2, **kwargs, kwargs40):
#     pass

# There shouldn't be any arguments after **kwargs
# def print_args(arg1, arg2, *args, kwarg1, kwarg2, **kwargs, kwargs40):
#                                                             ^
# SyntaxError: invalid syntax
