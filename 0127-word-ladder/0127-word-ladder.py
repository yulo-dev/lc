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
            for _ in range(len(queue)):  # 同一層（同一步數）
                word = queue.popleft()
                if word == endWord:
                    return distance

                for new_word in self.get_next_word(word):  # 產生所有「差一個字母」候選
                    if new_word not in wordset or new_word in visited:
                        continue
                    queue.append(new_word)
                    visited.add(new_word)
            distance += 1

        return 0


    #產生所有「只改一個字母」的候選單字
    def get_next_word(self, word):
        words = []

        for i in range(len(word)):
            left = word[:i]
            right = word[i + 1:]
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                if ch == word[i]:
                    continue
                words.append(left + ch + right)
                
        return words