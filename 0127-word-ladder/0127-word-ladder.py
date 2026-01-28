from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:

        #I convert wordList into a set so I can validate neighbors in constant time, because during BFS I’ll generate 
        #many candidate words and I need to quickly test whether a candidate exists in the dictionary.
        #If I kept it as a list, the in check would be O(N) each time, which would be too slow given we generate 
        #up to 26·L neighbors per word.
        
        wordset = set(wordList)

        if endWord not in wordset:
            return 0

        dist = 1
        queue = deque([(beginWord)])
        visited = set([beginWord])

        while queue:
            for _ in range(len(queue)): # process one BFS level
                 word = queue.popleft()
                 if word == endWord:
                    return dist
                 for next_word in self.find_word(word):
                    if next_word not in wordset or next_word in visited:
                        continue
                    queue.append(next_word)
                    visited.add(next_word)
            dist += 1 # each level, dist + 1

        return 0


    #For a word, I generate all its neighbors by changing each character position to a..z (except the original char). 
    #If the generated word exists in wordSet and hasn’t been visited, I push it into the queue.
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
