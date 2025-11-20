import re
from collections import Counter

class Tokeniser:

    def tokenise(self, text: str) -> list[str]:
        if type(text) != str:
            return 'Input text must be a string'
        else:
            lower_text = text.lower()
            words = [word for word in re.split(r'[ .,;"\'/()!?:]+', lower_text) if word]
            return words
    
    def count_tokens(self, tokens: list[str]) -> dict[str, int]:
        counter = Counter()
        for word in tokens:
            counter[word] += 1
        return counter
        
