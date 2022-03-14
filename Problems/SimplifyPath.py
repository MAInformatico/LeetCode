class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        path = path.split('/')
        for i in path:
            if i:
                if i==".":
                    continue
                elif i=="..":
                    if result:
                        result.pop()
                else:
                    result.append(i)
        return "/"+"/".join(result)
