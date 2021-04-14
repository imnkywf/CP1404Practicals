words_list = ("this", "is", "a", "collection", "of", "words", "of" ,"nice", "words", "this", "is", "a", "fun", "thing", "it", "is")

count = {}

for word in words_list:
    try:
        count[word] += 1
    except KeyError:
        count[word] = 1
for k, v in count.items():
    print("{:10} : {}".format(k, v))



