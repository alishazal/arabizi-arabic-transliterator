import itertools

d = {
    "k": [{"ك": 1}],
    "i": [{"": 0.4}, {"ي": 0.3}, {"ى": 0.3}],
    "t": [{"ت": 0.7}, {"تا": 0.3}],
    "a": [{"": 0.1}, {"ا": 0.6}, {"ه": 0.1}, {"ة": 0.2}],
    "b": [{"ب": 1}]
}

def sortByDictValue(dict):
    return dict["probability"]

def product(*args, repeat=1):
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    
    for pool in pools:
        result = [x+[y] for x in result for y in pool]

    ret = []
    for prod in result:
        # Initialiaze probability with 1=
        probability = 1
        combinedStr = ""
        # Calculating overall probability for string and combining individual letters
        # to form full string
        for ele in prod:
            probability *= list(ele.values())[0]
            combinedStr += list(ele.keys())[0]

        ret.append({"string": combinedStr, "probability": probability})

    ret.sort(key=sortByDictValue, reverse=True)
    return ret

def arabiziToArabic(inputStr):
    
    l = []
    for i in inputStr:
        l.append(d[i])


    arabicPossibilities = product(*l)
    for i in arabicPossibilities:
        print(i)

# print(arabiziToArabic("kitab"))
arabiziToArabic("kitab")