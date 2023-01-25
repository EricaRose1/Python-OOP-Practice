"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    '''finds random words from dictionary
    >>> wf = WordFinder("simple.txt")
    3 words read
    
    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    
    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
     
    >>> wf.random() in ["cat", "pig", "porcupine"]
    False
    '''
    def __init__(self, path):
        '''Returns number of items read.'''
        dict_file = open(path)
        self.words = self.parse(dict_file)

        print(f'{len(self.words)} words read')

    def parse(self, dict_file):
        '''parse dict_file -> list of words.'''
        return [w.strip() for w in dict_file]
    
    def random(self):
        '''Return random word.'''
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    '''Word finder that excludes blank lines&comments

    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    False

    >>> swf.random() in ["apple", "parsnips", "kale"]
    True

    >>> swf.random() in ["parsnips", "mango", "kale"]
    True
    '''
    def parse(self, dict_file):
        '''parse dict_file -> list of words, skipping blanks and comments.'''
        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]