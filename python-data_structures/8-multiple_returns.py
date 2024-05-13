#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return(len(sentence), None)
    return tuple((len(sentence), sentence[0]))


sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))