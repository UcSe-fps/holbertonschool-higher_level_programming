#!/usr/bin/python3
"""
right
"""
import pickle


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        """
        Initializes the CustomObject with name, age, and student status.
        """
        self.name = name
        self.age = age
        self.is_student = is_student
        
        def display:
            """
        Prints the object's attributes in a formatted manner.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

        def serialize(self, filename):
            """
            Serializes the current instance to a file using pickle.

        Args:
            filename (str): The name of the file to save the object to.
            """
            try:
                with open(filename, 'wb', encoding='utf-8') as f:
                    pickle.dump(self, f)
            except Exception:
                return None

        @classmethod
        deserialize(cls, filename):
            """
            Loads an instance of CustomObject from a file using pickle.

        Args:
            filename (str): The name of the file to load the object from.

        Returns:
            CustomObject: The deserialized object or None if an error occurs.
            """
            try:
                with open(filename, 'rb', encoding='utf-8') as f:
                    return pickle.load(cls, f)
            except (FileNotFoundError, pickle.UnpicklingError, EOFError, Exception):
                return None
