# message = "global"
#
#
# def enclosing():
#     message = "enclosing"
#
#     def local():
#         message = "local"
#         print("local message", message)
#
#     print("Enclosing message", message)
#     local()
#     print("Enclosing message", message)
#
#
# print("Global message", message)
# enclosing()
# print("Global message", message)

# Answer:
# Global message global
# Enclosing message enclosing
# local message local
# Enclosing message enclosing

# message = "global"
#
#
# def enclosing():
#     message = "enclosing"
#
#     def local():
#         global message  #we can bind global message into local.
#                         # Here global modifies the binding in local
#         message = "local"
#         # print("local message", message)
#
#     print("Enclosing message", message)
#     local()
#     print("Enclosing message", message)
#
#
# print("Global message:1", message)
# enclosing()
# print("Global message", message)

# Answer:-

# Global message:1 global
# Enclosing message enclosing
# Enclosing message enclosing
# Global message local

message = "global"


def enclosing():
    message = "enclosing"

    def local():
        nonlocal message  #we can bind enclosing scope into local namespace.
                          #Searches enclosing scope from inner most to outer most
        message = "local"
        # print("local message", message)

    print("Enclosing message:1", message)
    local()
    print("Enclosing message", message)


print("Global message:1", message)
enclosing()
print("Global message", message)

# Answers:-
# Global message:1 global
# Enclosing message:1 enclosing
# Enclosing message local
# Global message global