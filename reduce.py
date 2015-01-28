newDict = {}
reducable_words = []
reduced_pairs = {}
current_word = ""


with open('words.txt', 'r') as f:
    for line in f:
        word = line.strip().lower()
        newDict[word] = len(word)


def is_word(word):
    return word in newDict


def get_reduced_variations(word):
    variations = []
    word = list(word)
    for index in range(0, len(word)):
        variations.append("".join(word[:index] + word[index + 1:]))
    return variations


def save_if_reducable(word, path):
    for variation in get_reduced_variations(word):
        if variation is "":
            reducable_words.append(path)
        if is_word(variation):
            path.append(variation)
            save_if_reducable(variation, path)

for entry in newDict:
    save_if_reducable(entry, [entry])

for path in reducable_words:
    reduced_pairs[path[0]] = path

real_words = reduced_pairs.keys()
print sorted(real_words, key=len)
