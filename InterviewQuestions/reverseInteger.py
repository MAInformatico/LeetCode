class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            reverseNumber = int('-' + x[-1:0:-1])
            if reverseNumber >= -2147483648 and reverseNumber <= 2147483647:
                return reverseNumber
            else:
                return 0
        else:
            reverseNumber = int(x[::-1])
            if reverseNumber >= -2147483648 and reverseNumber <= 2147483647:
                return reverseNumber
            else:
                return 0
