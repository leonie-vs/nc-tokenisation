from tokeniser import Tokeniser

# Test 1
def test_tokenise_returns_list_of_string_input():
    t = Tokeniser()
    output = t.tokenise("hello")
    assert output == ["hello"]

# Test 2
def test_tokeniser_gives_error_when_input_not_str():
    t = Tokeniser()
    num = t.tokenise(0)
    list_input = t.tokenise(['hello'])
    assert num == 'Input text must be a string'
    assert list_input == 'Input text must be a string'