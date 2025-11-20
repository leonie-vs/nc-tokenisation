import re

class Tokeniser:

    def tokenise(self, text: str) -> list[str]:
        if type(text) == str:
            words = [word for word in re.split(r'[ .,!?:]+', text) if word]
            return words
        else:
            return 'Input text must be a string'
