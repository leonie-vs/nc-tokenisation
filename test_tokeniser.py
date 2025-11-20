from tokeniser import Tokeniser

# Test 1
def test_tokenise_returns_list_of_single_string_input():
    t = Tokeniser()
    output = t.tokenise("hello")
    assert output == ["hello"]
    assert type(output) == list

# Test 2
def test_tokeniser_gives_error_when_input_not_str():
    t = Tokeniser()
    num = t.tokenise(0)
    list_input = t.tokenise(['hello'])
    assert num == 'Input text must be a string'
    assert list_input == 'Input text must be a string'

# Test 3
def test_tokeniser_splits_multiple_input_words_based_on_spaces():
    t = Tokeniser()
    output = t.tokenise("hello world")
    assert output == ["hello", "world"]

# Test 4
def test_tokeniser_handles_extra_spaces_in_input():
    t = Tokeniser()
    output = t.tokenise("  hello    world")
    assert output == ["hello", "world"]
