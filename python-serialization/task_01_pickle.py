import pickle
'''Module for the class CustomObject'''


class CustomObject:
    '''class customobject using pickle module'''

    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except FileNotFoundError:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                return obj
        except FileNotFoundError:
            return None
