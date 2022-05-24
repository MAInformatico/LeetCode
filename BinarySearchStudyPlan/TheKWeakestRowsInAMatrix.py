class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dictionary = {}
        List = []
        for i in mat:
            count = 0
            for j in i:
                if j == 1:
                    count += 1
            List.append(count)
            
        for i in range(len(List)):
            dictionary[i] = List[i]
        
        return [i[0] for i in sorted(dictionary.items(), key = lambda i: i[1])[:k]]
