# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left,right = 1,n
        while left <= right:
            middle = (left+right)//2
            if guess(middle) == 0:
                return middle
            if guess(middle) < 0:
                right = middle -1
            else:
                left = middle + 1
        return -1
