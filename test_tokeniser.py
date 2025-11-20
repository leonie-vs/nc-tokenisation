from tokeniser import Tokeniser

# Test tokenise method of Tokeniser class
# Test 1
def test_tokenise_returns_list_of_single_string_input():
    t = Tokeniser()
    output = t.tokenise("hello")
    assert output == ["hello"]
    assert type(output) == list

# Test 2
def test_tokenise_gives_error_when_input_not_str():
    t = Tokeniser()
    num = t.tokenise(0)
    list_input = t.tokenise(['hello'])
    assert num == 'Input text must be a string'
    assert list_input == 'Input text must be a string'

# Test 3
def test_tokenise_splits_multiple_input_words_based_on_spaces():
    t = Tokeniser()
    output = t.tokenise("hello world")
    assert output == ["hello", "world"]

# Test 4
def test_tokenise_handles_extra_spaces_in_input():
    t = Tokeniser()
    output = t.tokenise("  hello    world")
    assert output == ["hello", "world"]

# Test 5 
def test_tokenise_splits_by_multiple_delimiters():
    t = Tokeniser()
    output = t.tokenise("hello world!  ! this is, a sentence? with: punctuation.")
    assert output == ["hello", "world", "this", "is", "a", "sentence", "with", "punctuation"]

# Test 6
def test_tokenise_converts_all_input_to_lowercase_before_tokenising():
    t = Tokeniser()
    output = t.tokenise("Hello world!")
    assert output == ["hello", "world"]


# Test count_tokens method of Tokeniser class
# Test 7
def test_count_tokens_returns_dict_with_str_keys_and_int_values():
    t = Tokeniser()
    output = t.count_tokens(["the", "cat", "in", "the", "hat"])
    assert output == {
        "the": 2,
        "cat": 1,
        "in": 1,
        "hat": 1
    }

# Test 8
def test_count_tokens_empty_dict_when_passed_empty_list():
    t = Tokeniser()
    output = t.count_tokens([])
    assert output == {}

# Test 9
def test_count_tokens_counts_all_tokens_in_passed_list():
    t = Tokeniser()
    input = ["the", "cat", "in", "the", "hat"]
    output = t.count_tokens(input)
    assert all(item in output for item in input) 


# Test sort_vocab method of Tokeniser class
# Test 10
def test_sort_vocab_returns_list_of_tuples():
    t = Tokeniser()
    output = t.sort_vocab({"the": 2, "cat": 1, "in": 1, "hat": 1})
    assert type(output) == list
    assert type(output[0]) == tuple
    assert len(set(type(x) for x in output)) == 1

# Test 11
def test_sort_vocab_sorts_tuples_in_desc_order():
    t = Tokeniser()
    output = t.sort_vocab({"the": 2, "cat": 1, "in": 5, "hat": 1})
    assert output == [("in", 5), ("the", 2), ("cat", 1), ("hat", 1)]


# Test split_into_subwords method of Tokeniser class
# Test 12
def test_split_into_subwords_returns_list_of_lists():
    t = Tokeniser()
    output = t.split_into_subwords(["cat"])
    assert type(output) == list
    assert type(output[0]) == list
    assert len(set(type(x) for x in output)) == 1

# Test 13
def test_split_into_subwords_returns_characters_with_end_symbol():
    t = Tokeniser()
    result = t.split_into_subwords(["cat"])
    assert result == [["c", "a", "t", Tokeniser.END_OF_WORD_SYMBOL]]
    assert Tokeniser.END_OF_WORD_SYMBOL == "</w>"

# Test 14 
def test_split_into_subwords_handles_empty_input_list():
    t = Tokeniser()
    result = t.split_into_subwords([])
    assert result == 'Empty input list'


# Test count_symbol_pairs method of Tokeniser class
# Test 15
def test_count_symbol_pairs_returns_dict_with_tuple_keys_and_int_values():
    t = Tokeniser()
    subwords = [
        ["c", "a", "t", "</w>"],
        ["c", "a", "r", "</w>"],
        ["t", "a", "c", "</w>"]
    ]
    result = t.count_symbol_pairs(subwords)
    assert result[("c", "a")] == 2
    assert result[("a", "t")] == 1
    assert result[("a", "r")] == 1
    assert result[("t", "a")] == 1
    assert result[("a", "c")] == 1

# Test 16
def test_count_symbol_pairs_returns_empty_dict_when_passed_empty_list():
    t = Tokeniser()
    output = t.count_symbol_pairs([])
    assert output == {}