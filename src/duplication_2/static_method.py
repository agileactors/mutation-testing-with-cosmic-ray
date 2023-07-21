class SomeClass:

    def __init__(self, some_dependency):
        self.some_dependency = some_dependency

    @staticmethod
    def static_method():
        pass

    def a_method(self):
        if self.some_dependency == 5:
            return "some_dependency is 5"
        else:
            return "some_dependency is not 5"
