# Tokenisation - Byte Pair Encoding (BPE) 

**Repo Layout:**

- Dependencies in **requirements.txt**
- Tokeniser class in **tokeniser.py**
- Tests for class in **test_tokeniser.py**, can be performed using Pytest

**Tokeniser class:**

- Create a Tokeniser instance: tokeniser = Tokeniser()

**tokenise()**
- Generate a list of words from a string by calling **tokeniser.tokenise("This is an example")**. This method seperates the input string into separate word strings (tokens). All tokens are converted to lowercase, and the method splits the input text by spaces and punctuations (.,;"\'/()!?:). 
- Example output: ["this", "is", "an", "example"]

**split_into_subwords()**
- Split these tokens into subwords by calling **tokeniser.split_into_subwords(tokens_list)**, passing the list generated with the tokenise() method as an argument. This will generate a list where each item is another list holding a token split into characters. The last item of each of these nested lists is the class-level constant END_OF_WORD_SYMBOL, which symbolises the end of each token. 
- Example output: [<br> 
    ["t", "h", "i", "s" "</'w>"],<br> 
    ["i", "s", </'w>"],<br> 
    ["a", "n", </'w>"],<br>
    ["e", "x", "a", "m", "p", "l", "e", "</'w>"]<br>
    ]

**count_tokens()**
- Count how many times each token appears by calling **tokeniser.count_tokens(tokens_list)**
- Returns a dictionary mapping each token to its frequency.
- Useful for analysing vocabulary distribution.
- Example output: {"this": 1, "is": 1, "an": 1, "example": 1}

**sort_vocab()**
- Sort a token frequency dictionary by calling **tokeniser.sort_vocab(token_counts)**
- Returns a list of (token, count) tuples ordered by descending frequency.
- Helpful for identifying the most common tokens.
- Example output: [("example", 1), ("this", 1), ("is", 1), ("an", 1)]

**count_symbol_pairs()**
- Identify all adjacent symbol pairs in the subword token list produced by split_into_subwords()
- Call with **tokeniser.count_symbol_pairs(subword_tokens)**
- Returns a dictionary mapping each symbol pair (a, b) to its frequency across the corpus.
- Forms the basis of the BPE merge step.
- Example output: {("e", "x"): 1, ("x", "a"): 1, ...}

**merge_most_frequent_pair()**
- Merge the most frequently occurring adjacent symbol pair in the current subword tokens.
- Call with **tokeniser.merge_most_frequent_pair(subword_tokens, pair_counts)**
- All occurrences of the highest-frequency pair (a, b) are replaced by the merged symbol a+b.
- Returns an updated list of subword tokens after the merge step.

**build_bpe_vocab()**
- Apply Byte Pair Encoding iteratively to build a more expressive subword vocabulary.
- Call with tokeniser.build_bpe_vocab(tokens_list, num_merges), specifying how many merge steps to run.
- The method repeatedly:
    - Counts symbol pairs
    - Identifies the most frequent pair
    - Merges that pair into a new subword
    - Returns the final subword representation after all merge operations.
- Example: with tokens ["aa", "ab", "aa"] and 2 merges, the result becomes:<br>[["aa</w>"], ["a", "b", "</w>"], ["aa</w>"]]
