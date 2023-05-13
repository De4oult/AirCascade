from random import choice

words: list[str] = ['Hello', 'I love you', 'See ya later', 'Goodbye']
names: list[str] = ['Tim', 'World', 'John', 'Mary']

with open('./res/test.txt', 'a') as file:
    file.write('%s, %s!\n' % (choice(words), choice(names)))