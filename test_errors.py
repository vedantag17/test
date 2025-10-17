# Test code with intentional errors for testing purposes

# Syntax error: missing colon after def
def hello_world
    print("Hello, World!")

# Indentation error
if True:
print("This will cause an IndentationError")

# NameError: undefined variable
print(undefined_variable)

# TypeError: cannot add string and int
result = "string" + 5
print(result)

# ZeroDivisionError
division = 10 / 0
print(division)

# ImportError: importing non-existent module
import nonexistent_module

# AttributeError: calling method on None
none_value = None
none_value.some_method()

# IndexError: accessing out of range
my_list = [1, 2, 3]
print(my_list[10])

# KeyError: accessing non-existent key
my_dict = {"a": 1}
print(my_dict["b"])

# ValueError: invalid literal for int
number = int("not_a_number")

# AssertionError: failing assertion
assert 1 == 2, "This assertion will fail"