class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:                
        dictionary = defaultdict(list)
        for x,y in pairs:
            dictionary[x].append(y)
            dictionary[y].append(x)

        def DFS(x,listA): #https://en.wikipedia.org/wiki/Depth-first_search
            if x in dictionary:
                listA.append(x)
                for y in dictionary.pop(x):
                    DFS(y,listA)

        s    = list(s)
        while dictionary:
            x = next(iter(dictionary))
            listA = []
            DFS(x,listA)
            listA = sorted(listA)
            listB = sorted([ s[i] for i in listA ])
            for i,v in enumerate(listB):
                s[listA[i]] = v
        return ''.join(s)
