import pickle
'''Module for the class CustomObject'''


class CustomObject:
    '''class customobject using pickle module'''

    def __init__(self, name: str, age: int, is_student: bool):
        '''constructor for the class CustomObject'''
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        '''method display, prints the instances of the class'''
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        '''method that serializes the object into a file'''
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except FileNotFoundError:
            return None

    @classmethod
    def deserialize(cls, filename):
        '''method that deserializes an object from a file'''
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                return obj
        except FileNotFoundError:
            return None
