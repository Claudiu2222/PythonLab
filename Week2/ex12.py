def get_words_that_rhyme(words):
    last_two_letters = set()
    for word in words:
        if len(word) >= 2:
            last_two_letters.add(word[-2:])
        else:
            last_two_letters.add(word)

    rhyming_couples = dict()

    for word in words:
        if len(word) >= 2:
            if word[-2:] in last_two_letters:
                if word[-2:] in rhyming_couples:
                    rhyming_couples[word[-2:]].append(word)
                else:
                    rhyming_couples[word[-2:]] = [word]
    return list(rhyming_couples.values())


print(get_words_that_rhyme((["ana", "banana", "carte", "arme", "parte"])))
