class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes
        self.children = {}
        # Boolean to indicate if this node marks the end of a word
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        # Root node of the trie
        self.root = TrieNode()

    def insert(self, word):
        """Inserts a word into the trie."""
        node = self.root
        for char in word:
            # If the character is not already a child, add it
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the next node
            node = node.children[char]
        # Mark the end of the word
        node.is_end_of_word = True

    def search(self, word):
        """Searches for a word in the trie. Returns True if found, False otherwise."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        """Returns True if any word in the trie starts with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def get_words_with_prefix(self, prefix):
        """Finds all words in the trie that start with the given prefix."""
        def dfs(node, prefix, words):
            if node.is_end_of_word:
                words.append(prefix)
            for char, child_node in node.children.items():
                dfs(child_node, prefix + char, words)

        # Start from the node matching the prefix
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []  # No words match the prefix
            node = node.children[char]

        # Collect all words starting from this node
        words = []
        dfs(node, prefix, words)
        return words


if __name__ == '__main__':
    # Example Usage
    trie = Trie()
    trie.insert("cat")
    trie.insert("cap")
    trie.insert("dog")
    trie.insert("dot")
    trie.insert("cart")

    print(trie.search("cat"))  # True
    print(trie.search("car"))  # False
    print(trie.starts_with("ca"))  # True
    print(trie.get_words_with_prefix("ca"))  # ['cat', 'cap', 'cart']
    print(trie.get_words_with_prefix("car"))
    print(trie.get_words_with_prefix("do"))  # ['dog', 'dot']
