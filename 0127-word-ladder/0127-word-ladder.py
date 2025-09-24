from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:

        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue = deque([beginWord])
        visited = set([beginWord])
        distance = 1

        while queue:
            for i in range(len(queue)): # 內層 for：確保「一層處理完後才 +1 距離」。
                word = queue.popleft()
                if word == endWord:
                    return distance

                for next_word in self.get_next_words(word):
                    if next_word in wordSet and next_word not in visited:
                        queue.append(next_word)
                        visited.add(next_word)
            
            distance += 1
        return 0
                
    def get_next_words(self, word):
        words = []

        for i in range(len(word)):
            left = word[:i]
            right = word[i+1:]
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == ch:
                    continue
                words.append(left + ch + right)
        return words