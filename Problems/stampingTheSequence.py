class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        lenTarget, lenStamp = len(target),len(stamp)
        move = 0
        maxmove = 10*lenTarget
        result = []
        def checker(string):
            for i in range(lenStamp):
                if string[i] == stamp[i] or string[i] == '?':
                    continue
                else:
                    return False
            return True
        
        while move < maxmove:
            premove = move
            for i in range(lenTarget - lenStamp+1):
                if checker(target[i:i+lenStamp]):
                    move += 1
                    result.append(i)
                    target = target[:i] + "?"*lenStamp + target[i+lenStamp:]
                    if target == "?"*lenTarget :
                        return result[::-1]
            if premove == move:
                return []
        return []
