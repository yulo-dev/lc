from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordset = set(wordList)
        if endWord not in wordset:
            return 0

        queue = deque([beginWord])
        visited = set([beginWord])
        dist = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return dist
                for new_word in self.create_word(word):
                    if new_word not in wordset or new_word in visited:
                        continue
                    if new_word == endWord:
                        return dist + 1
                    queue.append(new_word)
                    visited.add(new_word)
            dist += 1

        return 0

    def create_word(self, word):
        words = []
        for i in range(len(word)):
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                left = word[:i]
                right = word[i+1:]
                if ch == word[i]:
                    continue
                words.append(left + ch + right)

        return words
