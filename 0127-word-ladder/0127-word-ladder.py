from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        #I converted the wordList into a set to optimize lookup performance. 
        #In Python, checking for existence in a list takes O(N) time because it requires a linear scan. 
        #However, a set lookup is an O(1) operation on average because it's implemented using a hash table. 
        #Since our BFS performs this check for every generated mutation, using a set is essential to prevent a Time Limit Exceeded (TLE) error.
        wordset = set(wordList)

        if endWord not in wordset:
            return 0

        # The queue and the visited set are the two fundamental components of this BFS algorithm.
        # First, the queue manages our search frontier. It stores the words that are waiting to be explored.
        # Since BFS follows a FIFO (First-In-First-Out) structure, the queue ensures we process the words level-by-level. 
        # This is exactly how we guarantee that the first time we hit the endWord, it’s via the shortest path.
        queue = deque([beginWord])


        # the visited set acts as the memory of our search. It keeps track of all the words we have already encountered. 
        #Its main purpose is to prevent cycles and redundant computations.
        visited = set([beginWord])

        #The queue tells the algorithm where to go next, while the visited set tells it where not to go back.

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
                        return dist + 1 #提早結束
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
