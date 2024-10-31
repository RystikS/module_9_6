def all_variants(text):
    for i in range(len(text)):
        word = []
        word.append(text[i])
        for j in range(i, len(text)):
            if j != i:
                word.append(text[j])
            yield ''.join(word)


a = all_variants("abc")
for i in a:
    print(i)