#!/usr/bin/python3

def multiple_returns(sentence):
    s_len = len(sentence)
    if s_len == 0:
        return (0, None)
    else:
        present = (s_len, sentence[0])
        return present
