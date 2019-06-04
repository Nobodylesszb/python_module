from test_patterns import test_patterns

test_patterns(
    'This is some text -- with punctuation.',
    [('[^-. ]+', 'sequences without -, ., or space')],
)

#This pattern finds all of the 
# substrings that do not contain the characters -, ., or a space.