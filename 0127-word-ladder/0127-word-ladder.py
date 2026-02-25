from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordset = set(wordList)
        if endWord not in wordset:
            return 0

        queue = deque([beginWord])
        visited = set([beginWord])
        dist = 1 # 起點算第一步

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return dist

                for new_word in self.generate_word(word):
                    if new_word not in wordset or new_word in visited:
                        continue
                    if new_word == endWord:
                        return dist + 1 #提早結束
                    queue.append(new_word)
                    visited.add(new_word)
            dist += 1

        return 0

    def generate_word(self, word):
        new_word = []
        for i in range(len(word)):
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == ch:
                    continue
                new_word.append(word[:i] + ch + word[i+1:])
        return new_word