class PrefixTree:

    def __init__(self):
        self.children = {}
        self.word = False

    def insert(self, word: str) -> None:
        cur = self
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = PrefixTree()
            cur = cur.children[letter]
        cur.word = True

    def search(self, word: str) -> bool:
        cur = self
        for letter in word:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return cur.word
        
    def startsWith(self, prefix: str) -> bool:
        cur = self
        for letter in prefix:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return True
        