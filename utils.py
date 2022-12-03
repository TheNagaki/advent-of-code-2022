# Some types
some_string = "Hello World"
some_int = 42
some_float = 3.14
some_bool = True
some_list = [1, 2, 3, 4, 5]
some_dict = {"name": "John", "age": 42}
some_tuple = (1, 2, 3, 4, 5)
some_set = {1, 2, 3, 4, 5}


# How do you define a function?
def some_function():
    return "Hello World"


# How do you define a class?
class SomeClass:
    def __init__(self, name):
        self.name = name

    def some_method(self):
        return "Hello World"


# How do you define a class with inheritance?
class SomeChildClass(SomeClass):
    def __init__(self, name):
        super().__init__(name)

    def some_method(self):
        return "Hello World"


# How do you define an interface?
class SomeInterface:
    def some_method(self):
        pass


# How do you define a class that implements an interface?
class SomeClassImplementingInterface(SomeInterface):
    def some_method(self):
        return "Hello World"
