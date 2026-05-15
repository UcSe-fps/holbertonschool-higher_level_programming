#!/usr/bin/python3
import pickle

class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object attributes in a specific format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the current instance to a file using pickle."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, IOError) as e:
            print(f"Error saving file: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """Loads a CustomObject instance from a file."""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError) as e:
            # Returns None if the file is missing, empty, or corrupted
            return None
        except Exception as e:
            return None
