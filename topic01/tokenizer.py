# tokenizer.py 
# Created: 8/20/2025
# Last Edit: 8/20/2025
# Yury Sergeev

import re

patterns = [

    [r"\d*\.\d+|\d\.\d*|\d+", "number"], #int, float, and int dot (1, 1.123, 1.)
    [r"\+", "+"],                        # + sign recognition
    [r".","error"]                       #Nothing matched therfore error

]

for pattern in patterns:
    pattern[0] = re.compile(pattern[0])

def tokenize(characters):
    tokens = []
    position = 0
    while position < len(characters):
        #find first token match
        for pattern, tag in patterns:
            match = pattern.match(characters, position)
            if match:
                break

        assert match

        if tag =="error":
            raise Exception(f"Syntax Error: illegal char:{[match.group(0)]}")

        token = {"tag":tag, "position":position}
        value = match.group(0)
        if token["tag"] == "number":
            if "." in value:
                token["value"] == float(value)
            else: 
                token["value"] == int(value)

        tokens.append(token)
        position = match.end()

    tokens.append({"tag":None, "position":position})
    return tokens

def test_simple_tokens():
    print("test_simple_tokens...")
    assert tokenize("+") == [ 
        {"tag":"+", "position":0},
        {"tag":None, "position":1}
    ]

    print("test_simple_token...")
    assert tokenize("3") == [ 
        {"tag":"number", "position":0, "value":3}
        {"tag":None, "position":1}
    ]


if __name__ == "__main__":

    print("Testing the Tokenizer...")

    test_simple_tokens()


    print("Done testing Tonkenizer.")