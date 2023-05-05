def encode(string_list):
    encoded_string = ''
    delimiter = '&'
    for s in string_list:
        encoded_string += f'{len(s)}{delimiter}{s}'
    return encoded_string


def decode(encoded_string):
    res = []
    i = 0
    while i < len(encoded_string):
        j = i
        while encoded_string[j] != '&':
            j += 1
        length = int(encoded_string[i:j])
        end = j + length + 1
        string_val = encoded_string[j+1: end]
        res.append(string_val)
        i = end
    return res



if __name__ == "__main__":
    input = ["lintlintlintlintlintlintlintlint", "code", "love", "you"]
    encoded_string = encode(input)
    print(encoded_string)

    print(decode(encoded_string))

    input = ["lint", "code", "love", "you", ""]
    encoded_string = encode(input)
    print(encoded_string)

    print(decode(encoded_string))

