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
        if corp[0] not in passes:
            passes[corp[0]] = [corp[1]]
        else:
            passes[corp[0]].append(corp[1])
    return passes


def validate(data):
    valid = 0
    passwcount = 0
    for k,v in data.items():
        passwcount += len(v)
        for x in v:
            ct = 0
            for ch in x:
                if k[2] == ch:
                    ct += 1
            if int(k[0]) <= ct <= int(k[1]):
                valid += 1
    if passwcount != 1000:
        print("values missing")
    return valid

def positions(data):
    valid = 0
    for k, v in data.items():
        for x in v:
            if x[int(k[0])] == k[2] and x[int(k[1])] != k[2]:
                valid += 1
            elif x[int(k[1])] == k[2] and x[int(k[0])] != k[2]:
                valid += 1
            else:
                pass
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
    actual = positions(dict)
    print(actual)
