class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        regex = re.compile("(\w+.txt)\((.*?)\)", re.IGNORECASE)
        dictionary = defaultdict(list)
        
        for i in paths:
            root = i.split(" ")[0]
            file = re.findall(regex, i)
            
            for name, content in file:
                dictionary[content].append(root + "/" + name)
        
        return list(filter(lambda x: len(x)>1, dictionary.values()))
