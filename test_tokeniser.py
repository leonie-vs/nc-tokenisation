from tokeniser import Tokeniser

# Test 1
def test_tokenise_returns_list_of_string_input():
    t = Tokeniser()
    output = t.tokenise("hello")
    assert output == ["hello"]

