# tokenizer.py
# Yury Sergeev
# Created: 8/20/2025
# Updated: 8/20/2025

# This is a tokenizer for a custom programming language built in class/as an assignment
# for CS33101-Structure Of Programming Languages

import re

patterns = [
    [r"\d*\.\d+|\d+\.\d*|\d+","number"],  # int, float.nums, float.none
    [r"\+", "+"],                         # plus (+)
    [r".","error"]                        # none found -> error
]

for pattern in patterns:
    pattern[0] = re.compile(pattern[0])

def tokenize(characters):
    tokens = []
    position = 0
    while position < len(characters):
        # find first matching token
        for pattern, tag in patterns:
            match = pattern.match(characters, position)
            if match:
                break

        assert match

        if tag == "error":
            raise Exception(f"Syntax error: illegal character :{[match.group(0)]}")
    
        token = {"tag":tag, "position":position}
        value = match.group(0)
        if token["tag"] == "number":
            if "." in value:
                token["value"] = float(value)
            else:
                token["value"] = int(value)
        tokens.append(token)
        position = match.end()

    tokens.append({"tag":None, "position":position})
    return tokens

def test_simple_tokens():

    print("Testing simple tokens... \n.\n.\n.")

    # Test + operator
    assert tokenize("+") == [
        {"tag":"+", "position":0},
        {"tag":None, "position":1}
    ]
    print("+ operator - Pass")

    # Test int 
    assert tokenize("3") == [
        {"tag":"number", "position":0, "value":3},
        {"tag":None, "position":1}
    ]
    print("integer - Pass")


if __name__ == "__main__":
    print("testing tokenizer...")
    test_simple_tokens()
    print("done.")