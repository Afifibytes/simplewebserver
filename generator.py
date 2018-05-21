import random

class Generator:
    """
    Number Generator for integers, interval of [start, end] with n elements
    """
    def __init__(self, elements, start, end):
        self.listOfNumbers = []
        self.elements = elements
        self.start = start
        self.end = end

    def generate(self):
        """returns list with n random integers"""
        for i in range(self.elements):
            self.listOfNumbers.append(random.randrange(self.start, self.end))
        return self.listOfNumbers
        