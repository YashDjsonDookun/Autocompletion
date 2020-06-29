# Autocompletion
This problem was recently asked by AirBNB:

### Task: Implement auto-completion. Given a large set of words (for instance 1,000,000 words) and then a single word prefix, find all words that it can complete to.

```
class Solution:
  def build(self):
    # Fill this in.

  def autocomplete(self, word):
    # Fill this in.

s = Solution()
s.build(['dog', 'dark', 'cat', 'door', 'dodge'])
print(s.autocomplete('do'))
# ['dog', 'door', 'dodge']
```

### Usage:
`
    python3 autocomplete.py
`

If You want to test with 1,000,000:

    * 'pip3 install RandomWords'
    * uncomment this line: `from wordlist import words from autocomplete.py`
    * and uncomment this line too: `set_of_words = s.build(words)`

