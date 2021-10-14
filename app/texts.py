class Texts:
    def __init__(self):
        pass

    def textHome(self):
        t = """
        This is a simple application that consists
        of searching for similar words in a database
        with more than 260 thousand words in
        Portuguese-BR (ASCII format).
        The words are encoded in a matrix of 0's and
        1's called "WordFP", so the search for
        similarity is calculated based on the metrics:
        geometric, arithmetic, tanimoto and tversky.
        """
        return t
    
    def textContribute(self):
        t = """
        This app is free and opensource and you are very welcome to contribute.
        All source code can be accessed [here](https://github.com/jeffrichardchemistry/WordFP).
        """
        return t