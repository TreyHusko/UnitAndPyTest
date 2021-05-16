

def pal(input):
    word = input.lower()
    if (len(word) == 0):
        raise ValueError
    reverseWord = word[::-1]
    if (reverseWord != word):
        return False
    return True

