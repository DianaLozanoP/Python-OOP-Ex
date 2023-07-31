"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Takes the value of start"""
        self.start = start
        self.count = 0

    def generate(self):
        """Takes the start value, returns it first. 
        It starts to add 1 everytime the method is called."""
        if (self.count == 0):
            self.count += 1
            print(self.start)
        else:
            print(self.start + self.count)
            self.count += 1

    def reset(self):
        """It starts the count at 0."""
        self.count = 0


serial = SerialGenerator(start=100)
