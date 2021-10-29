from code_challenges.stack_queue_brackets.stack_queue_brackets import validate_brackets

def test():
    expected = False
    input_data="({}]"
    actual = validate_brackets(input_data)
    assert actual == expected
