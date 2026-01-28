from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordset = set(wordList)
        if endWord not in wordset:
            return 0

        dist = 1
        queue = deque([(beginWord)])
        visited = set([beginWord])

        while queue:
            for i in range(len(queue)):
                 word = queue.popleft()
                 if word == endWord:
                    return dist
                 for next_word in self.find_word(word):
                    if next_word not in wordset or next_word in visited:
                        continue
                    queue.append(next_word)
                    visited.add(next_word)
            dist += 1

        return 0
    
    def find_word(self, word):
        words = []

        for i in range(len(word)):
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                left = word[:i]
                right = word[i+1:]
                if ch == word[i]:
                    continue
                else:
                    words.append(left + ch + right)

        return words
