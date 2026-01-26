from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordset = set(wordList)
        if endWord not in wordset:
            return 0

        queue = deque([beginWord])
        visited = set([beginWord])
        distance = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return distance
                for new_word in self.find_new_word(word):
                    if new_word not in wordset or new_word in visited:
                        continue
                    queue.append(new_word)
                    visited.add(new_word)

            distance += 1

        return 0

    def find_new_word(self, word):
        words = []
        for i in range(len(word)):
            left = word[:i]
            right = word[i+1:]
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == ch:
                    continue
                words.append(left + ch + right)
                
        return words