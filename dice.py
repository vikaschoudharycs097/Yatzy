import random

class Dice:
    """
    Implementation of Dice

    It will take one optional arugment i.e. faces
    By defualt value of faces is 6

    Raise a ValueError if faces < 2
    Raise a TypeError if faces is not integer
    """
    def __init__(self, faces = 6):
        if not isinstance(faces, int):
            raise TypeError("Dice faces should be integer")
        elif faces < 2:
            raise ValueError("Dice faces should be greater than or equal to 2")
        else:
            self.__faces = faces

    def roll(self):
        return random.randint(1, self.__faces)

    def __str__(self):
        return f"Dice({self.__faces})"

    def __repr__(self):
        return f"Dice({self.__faces})"
