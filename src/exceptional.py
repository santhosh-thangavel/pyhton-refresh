import sys

DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def convert(s):


    try:
        number = ' '
        word_number = s.split()

        for word in word_number:

            number += DIGIT_MAP[word]
            return int(number)
    except (KeyError, AttributeError, TypeError) as e:
        print(f'conversion error: {e!r}', file=sys.stderr)


    # except KeyError:
    #     print("Conversion failed")
    #     x = -1
    # except TypeError:
    #     print("Conversion failed")
    #     x = -1
    # except AttributeError:
    #     print("Conversion failed")
    #     x = -1
    # print(x)
convert("Million one")