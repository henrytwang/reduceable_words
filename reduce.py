newDict = {}
reducable_words = []
current_word = ""


with open('words.txt', 'r') as f:
    for line in f:
        word = line.strip().lower()
        newDict[word] = len(word)


def is_word(word):
    return word in newDict


def save_if_reducable(word):
    if word is "":
        reducable_words.append(current_word)
    else:
        if is_word(word):
            save_if_reducable(word[:-1])


for key in newDict.keys():
    current_word = key
    save_if_reducable(current_word)
print sorted(reducable_words, key=len)