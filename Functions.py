import string
import collections


def eliminate(text):
    for i in string.punctuation:
        text = text.replace(i, " ")

    text = text.lower()
    text = text.split()
    return text


def create_index(dic):
    with open("index.txt", mode="w") as index:
        for k, v in dic.items():
            index.write(str(k)+" ---> { "+" ".join(map(str, v))+" }\n")
    save(dic, 'index')


def look_up(dic):
    val, val2 = input().split()
    with open("index_"+val+"_"+val2+".txt", mode="w") as lookup:
        lookup.write("from .I "+val+" to "+".I "+val2+" :\n")
        for i in range(int(val), int(val2)+1):
            lookup.write(" ".join(map(str, dic[i])))
            lookup.write("\n")


def create_inverse(dic):
    dic = collections.OrderedDict(sorted(dic.items()))

    with open("inverse.txt", mode="w") as inverse:
        for v, k in dic.items():
            inverse.write(v+" ---> "+" ".join(map(str, k)))
            inverse.write("\n")
    save(dic, 'inverse')


def save(data, name):
    import pickle

    with open(name + '.pik', 'wb') as w:
        pickle.dump(data, w)
