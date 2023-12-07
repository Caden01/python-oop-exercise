"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    """Machine that finds random words from a dictionary
    
    >>> word_finder = WordFinder("lesswords.txt")
    5 words read.  

    >>> word_finder.random() in ["purple", "orange", "yellow", "blue", "red"]
    True

    """

    def __init__(self, path) :
        """Reads through file and tells how many words were read."""
        
        file = open(path)

        self.words = self.parse(file)
        
        print(f"{len(self.words)} words read.")

    def parse(self, file) :
        """Creates a list of all the words from text file"""

        return [word.strip() for word in file]
    
    def random(self) :
        """Chooses a random word from the list of words."""

        return random.choice(self.words)

class SpecialWordFinder(WordFinder) :
    """Addition to word finder that ignores comments
    
    >>> special_word_finder = SpecialWordFinder("morewords.txt")
    6 words read.

    >>> special_word_finder.random() in ["blue", "pink", "yellow", "caden", "jacob", "pam"]
    True

    """

    def parse(self, file) :
        lst = []
        for word in file: 
            if word.strip() and not word.startswith("#") :
                lst.append(word.strip())

        return lst
