class Tokeniser:

    def tokenise(self, text: str) -> list[str]:
        if type(text) == str:
            words = text.split()
            return words
        else:
            return 'Input text must be a string'
