
def count(sentence):
    if (len(sentence) == 0):
        raise ValueError
    senLen = len(sentence.split())
    return senLen
