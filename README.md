# Tokenisation - Byte Pair Encoding (BPE) 

- Dependencies in **requirements.txt**
- Tokeniser class in **tokeniser.py**
- Tests for class in **test_tokeniser.py**, can be performed using Pytest

Tokeniser class:

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


