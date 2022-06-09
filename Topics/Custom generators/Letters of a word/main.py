def letters(word):
    for i in word:
        yield i


word = input()
iterator = letters(word)
for _ in range(len(word)):
    print(next(iterator))
