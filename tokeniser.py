import re
from collections import Counter

class Tokeniser:

    END_OF_WORD_SYMBOL = "</w>"

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
    
    def split_into_subwords(self, tokens: list[str]) -> list[list[str]]:
        if tokens == []:
            return 'Empty input list'
        subword_tokens = []
        for word in tokens:
            split_word = [ch for ch in word]
            split_word.append(self.END_OF_WORD_SYMBOL)
            subword_tokens.append(split_word)
        return subword_tokens
    
    def count_symbol_pairs(self, subword_tokens: list[list[str]]) -> dict[tuple[str, str], int]:
        adjacent_pairs = []
        for word in subword_tokens:
            for i in range(len(word) - 1):
                adjacent_pairs.append((word[i], word[i + 1]))
        pair_counts = Counter(adjacent_pairs)
        return pair_counts
    
    def merge_most_frequent_pair(self, subword_tokens: list[list[str]], pair_counts: dict[tuple[str, str], int]) -> list[list[str]]:        
        sorted_pairs = self.sort_vocab(pair_counts)
        most_frequent_pair = sorted_pairs[0][0]
        a, b = most_frequent_pair
        merged_tokens = []
        for token in subword_tokens:
            new_token = []
            i = 0
            while i < len(token):
                if i < len(token) - 1 and token[i] == a and token[i+1] == b:
                    new_token.append(a + b)
                    i += 2
                else:
                    new_token.append(token[i])
                    i += 1
            merged_tokens.append(new_token)
        return merged_tokens
        

        
