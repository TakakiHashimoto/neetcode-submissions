class TrieNode:
    def __init__(self):
        self.child = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    # This is the work of linking each character(TrieNode) to one another
    def addWord(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.child:
                current.child[char] = TrieNode()

            current = current.child[char]

        current.isEnd = True


    def search(self, word: str) -> bool:
        def dfs(node, index):
            # All pattern characters have been consumed
            if index == len(word):
                return node.isEnd

            char = word[index]

            # A normal letter: follow one child
            if char != ".":
                if char not in node.child:
                    return False

                return dfs(node.child[char], index + 1)

            # A dot: explore all possible children
            for child_node in node.child.values():
                if dfs(child_node, index + 1):
                    return True

            return False

        return dfs(self.root, 0)
