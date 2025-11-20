class Tokeniser:

    def tokenise(self, text: str) -> list[str]:
        if type(text) == str:
            return [text]
        else:
            return 'Input text must be a string'
