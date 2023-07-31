"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """Machine to retrieve a random word from a file.

    >>> wf = WordFinder("/home/dianaloz/python-oo-practice/words.txt")
    235886 words read

    """

    def __init__(self, file):
        """The attribute file is defined.
        We called the method get_words to create a list of words from the file"""
        self.file = file
        self.lst = self.get_words()
        print(f"{len(self.lst)} words read")

    def get_words(self):
        """File is open and words are appended to the list, while removing \n"""
        lst = []
        document = open(self.file, "r")
        for line in document.readlines():
            lst.append(line.rstrip("\n"))
        document.close()
        return lst

    def random(self):
        """Choose a random word from the list generated."""
        print(random.choice(self.lst))


class SpecialWordFinder(WordFinder):
    """An special word finder.  
    It will generate a random word while filtering empty spaces and comments."""

    def __init___(self, file):
        # get the parent class from above
        super().__init__(file)
        # change the method that will retrieve the list of words
        self.lst = self.get_filtered_words()

    def get_filtered_words(self):
        lst = []
        document = open(self.file, "r")
        for line in document.readlines():
            if (type(line) == str):
                if not (line.startswith("#")):
                    lst.append(line.rstrip("\n"))
        document.close()
        return lst


# wf = WordFinder("/home/dianaloz/python-oo-practice/words.txt")
