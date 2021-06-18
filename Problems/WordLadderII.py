import collections

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words=set(wordList)
        if endWord not in words:return[]
        words.add(beginWord)
        
        aux=defaultdict(set)
        
        for word in words:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    neww=word[:i]+c+word[i+1:]
                    if neww!=word and neww in words:
                        aux[word].add(neww)
                        aux[neww].add(word)
        
        
        distance=defaultdict(int)
        vis=set([beginWord])
        queue=deque([(beginWord,1)])
        while queue:
            curr,d=queue.popleft()
            distance[curr]=d
            for i in aux[curr]:
                if i not in vis:
                    queue.append((i,d+1))
                    vis.add(i)
        
        result=[]
        stack=[(beginWord,[beginWord])]
        while stack:
            curr,path=stack.pop()
            if curr==endWord and len(path)==distance[endWord]:
                result.append(path)
            for i in aux[curr]:
                if distance[i]>distance[curr]:
                    stack.append((i,path+[i]))
        
        return result
