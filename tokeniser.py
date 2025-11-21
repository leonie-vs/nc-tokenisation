import re
from collections import Counter

class Tokeniser:

    def __init__(self):
        self.vocab = set()

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
        for word in tokens:
            for ch in word:
                self.vocab.add(ch)
        self.vocab.add(self.END_OF_WORD_SYMBOL)
        return subword_tokens
    
    def count_symbol_pairs(self, subword_tokens: list[list[str]]) -> dict[tuple[str, str], int]:
        adjacent_pairs = []
        for word in subword_tokens:
            for i in range(len(word) - 1):
                adjacent_pairs.append((word[i], word[i + 1]))
        pair_counts = Counter(adjacent_pairs)
        return pair_counts
    
    def merge_most_frequent_pair(self, subword_tokens: list[list[str]], pair_counts: dict[tuple[str, str], int]) -> list[list[str]]:        
        if not pair_counts:
            return subword_tokens
        a, b = max(pair_counts, key=pair_counts.get)
        new_symbol = a + b
        self.vocab.add(new_symbol)
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
    
    def build_bpe_vocab(self, tokens: list[str], num_merges: int) -> list[list[str]]:
        subword_tokens = self.split_into_subwords(tokens)
        for i in range(num_merges):
            pair_counts = self.count_symbol_pairs(subword_tokens)
            if not pair_counts:
                break
            subword_tokens = self.merge_most_frequent_pair(subword_tokens, pair_counts)
        return subword_tokens
    
    def get_vocab(self) -> set[str]:
        return self.vocab
        

t = Tokeniser()
t.build_bpe_vocab(["cat", "car", "cart"], num_merges=5)

# After merging, this should include things like:
# {'c', 'a', 't', 'r', '</w>', 'ca', 'ar', 'car'}
print(t.get_vocab()) 
