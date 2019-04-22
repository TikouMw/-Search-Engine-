import Functions
import time


def main():
    start_time = time.time()
    with open("cacm.all") as file, open("common_words.txt") as not_this:
        not_this = set(not_this.read().splitlines())
        num = 1
        dic = {}
        dic_inverse = {}
        dic_inverse_poids = {}
        while True:
            text = ''
            line = file.readline()

            while line != ".T\n" and line != ".W\n" and line:
                line = file.readline()

            if not line:
                break

            while line != ".B\n" and line != ".A\n":
                text += line
                line = file.readline()

            text = Functions.eliminate(text)

            Non_double = list(set(text) - not_this)

            dic.update({num: Non_double})

            for word in Non_double:
                if word not in dic_inverse.keys():
                    dic_inverse.update({word: []})
                    dic_inverse_poids.update({word: []})
                index = dic[num].index(word)
                dic[num][index] = (word, text.count(word))
                dic_inverse[word].append((".I "+str(num), text.count(word)))
            dic[num] = sorted(dic[num], key=lambda x: (x[1], x[0]))
            num += 1
    Functions.create_index(dic)
    Functions.create_inverse(dic_inverse)

    print("--- %s seconds ---" % (time.time() - start_time))
    Functions.look_up(dic)


main()

