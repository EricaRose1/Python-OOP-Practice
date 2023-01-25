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
    def __init__(self, start=0):
        '''Make a generator, starting at start'''
        self.start = self.next = start
    
    def __rep__(self):
        ''' showing start and next'''
        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        '''Return Next'''
        self.next += 1
        return self.next -1

    def reset(self):
        '''Reset back to start'''
        self.next = self.start