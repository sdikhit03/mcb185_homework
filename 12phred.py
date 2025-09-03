# 12phred.py by Saumitra Dikhit

import math

def char_to_prob(symbol):           # convert phred quality symbol to error rate
    Q = ord(symbol) - 33                
    return 10 ** (-Q / 10)

def prob_to_char(prob):             # convert error rate to phred quality symbol
    if(prob > 0 and prob < 1):
        Q = round(-10 * math.log10(prob))
        return chr(Q + 33)


print(char_to_prob('A'))
print(char_to_prob('%'))
print(char_to_prob('g'))
print(prob_to_char(0.001))
print(prob_to_char(0.4))
print(prob_to_char(0))
print(prob_to_char(1))