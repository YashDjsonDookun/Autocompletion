from random_words import RandomWords
r = RandomWords()
words = r.random_words(count=5000)
for i in range(199):
    words = words + (r.random_words(count=5000))
