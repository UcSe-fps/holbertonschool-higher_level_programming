#!/usr/bin/python3
"""
right
"""
import pickle


class CustomObject:
    """
    A custom class representing a person with name, age, and student status.
    """


    def __init__(self, name, age, is_student):
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
        print("Name: {}". format(self.name))
        print("Age: {}". format(self.age))
        print("Is Student: {}". format(self.is_student))

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
