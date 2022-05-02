class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = dict()          
        for i in strs:
            sortedS = ''.join(sorted(s))
            dictionary[sortedS] = dictionary.get(sortedS, [])
            dictionary[sortedS] += [s]
        
        return dictionary.values()
