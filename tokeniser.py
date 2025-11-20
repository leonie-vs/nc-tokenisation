import re
from collections import Counter

class Tokeniser:

    def tokenise(self, text: str) -> list[str]:
        if type(text) != str:
            return 'Input text must be a string'
        else:
            lower_text = text.lower()
            tokens = [word for word in re.split(r'[ .,;"\'/()!?:]+', lower_text) if word]
            return tokens
    
    def count_tokens(self, tokens: list[str]) -> dict[str, int]:
        token_counts = Counter()
        for word in tokens:
            token_counts[word] += 1
        return token_counts
    
    def sort_vocab(self, token_counts: dict[str, int]) -> list[tuple[str, int]]:
        sorted_tokens = list(sorted(token_counts.items(), key=lambda item: item[1], reverse=True))
        return sorted_tokens
        
