class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
                
        curr.endofword = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(i, node):
            if i == len(word):
                return node.endofword
            letter = word[i]
            if letter == ".":
                for child in node.children.values():
                    if dfs(i+1, child):
                        return True
                return False
            else:
                if letter not in node.children:
                    return False
                return dfs(i+1, node.children[letter])
        return dfs(0, curr)

        
