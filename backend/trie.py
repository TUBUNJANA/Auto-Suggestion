import logging


class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = []  # (sentence, frequency)

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.sentence_freq = {}

    def insert(self, sentence: str):
        self.sentence_freq[sentence] = self.sentence_freq.get(sentence, 0) + 1
        logging.info(f"Inserting '{sentence}' with frequency {self.sentence_freq[sentence]}")
        node = self.root
        for char in sentence.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            self._update_sentences(node, sentence)

    def _update_sentences(self, node, sentence):
        if sentence not in [s for s, _ in node.sentences]:
            node.sentences.append((sentence, self.sentence_freq[sentence]))
        else:
            node.sentences = [
                (s, self.sentence_freq[s]) if s == sentence else (s, f)
                for s, f in node.sentences
            ]
        node.sentences.sort(key=lambda x: x[1], reverse=True)
        node.sentences = node.sentences[:10]
        logging.info(f"Updated node sentences: {node.sentences}")

    def search(self, prefix: str):
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                logging.info(f"Prefix '{prefix}' not found in trie.")
                return []
            node = node.children[char]
        suggestions = [s for s, _ in node.sentences]
        logging.info(f"Suggestions for '{prefix}': {suggestions}")
        return suggestions

    def to_dict(self):
        def node_to_dict(node):
            return {
                "sentences": node.sentences,
                "children": {char: node_to_dict(child) for char, child in node.children.items()}
            }
        return node_to_dict(self.root)