class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]

        for i in range(1,n+1):
            aux = [j + 2 ** (i - 1) for j in result][::-1]
            result += aux

        return result
