import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adj = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                l = word[:j] + "*" + word[j+1:]
                adj[l].append(word)
        seen = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word==endWord:
                    return res
                for j in range(len(word)):
                    l = word[:j] + "*" + word[j+1:]
                    for nei in adj[l]:
                        if nei not in seen:
                            seen.add(nei)
                            q.append(nei)

            res +=1
        return 0


#node -> wL[i] = for char in wL[i]

