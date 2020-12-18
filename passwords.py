"""
Created on 12/17/2020

@author: nadia
"""

def store_passwords(data):
    passes = {}
    for x in data:
        pw = x.split(":") # separate rule and password
        rule = pw[0].split() # separate numbers and letter
        maxmin = rule[0].split("-") # separate numbers
        corp = [(maxmin[0],maxmin[1],rule[1]), pw[1]]
        passes[corp[0]] = corp[1]
    return passes


def validate(data):
    valid = 0
    for k,v in data.items():
        ct = 0
        for x in v:
            if k[2] == x:
                ct += 1
        if int(k[0]) <= ct <= int(k[1]):
            valid += 1
    return valid


if __name__ == '__main__':
    f = open("pw.txt", "r")
    lines = []
    for x in f:
        lines.append(x[0:x.index("\n")])
    #sample = ["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"]
    #sampledict = store_passwords(sample)
    #print(validate(sampledict))
    dict = store_passwords(lines)
    correct = validate(dict)
    print(correct)