from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordset = set(wordList)
        if endWord not in wordList:
            return 0

        queue = deque([beginWord])
        visited = set([beginWord])
        distance = 1

        while queue:
            for _ in range(len(queue)): #同一個步數的字一起處理
                word = queue.popleft()
                if word == endWord:
                    return distance

                for new_word in self.valid_word(word):
                    if new_word not in wordset or new_word in visited:
                        continue

                    queue.append(new_word)
                    visited.add(new_word)
            distance += 1 #同個步數一起更新一次長度

        return 0

    def valid_word(self, word):
        words = []
        for i in range(len(word)):
            left = word[:i]
            right = word[i + 1:]
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                if ch == word[i]:
                    continue
                words.append(left + ch + right)

        return words