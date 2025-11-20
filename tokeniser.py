class Tokeniser:

    def tokenise(self, text: str) -> list[str]:
        if type(text) == str:
            words = [word for word in text.split() if word]
            return words
        else:
            return 'Input text must be a string'
