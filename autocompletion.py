#!/usr/bin/python3


#from wordlist import words // uncomment to import 1000000 words

class Solution:
    def build(self, listw):
        # Fill this in
        self.listw = listw
        return self.listw

    def autocomplete(self, word):
        # Fill this in
        self.word = word
        suggestions = []
        for i in range(len(set_of_words)):
            if ((set_of_words[i])[0:len(self.word)]) == self.word:
                suggestions.append(set_of_words[i])
        return suggestions
s = Solution()
set_of_words = s.build(['dog', 'dark', 'cat', 'door', 'dodge'])
#set_of_words = s.build(words) // uncomment to test with 1000000 words
print(s.autocomplete('do'))
#['dog', 'door',['dodge']]
