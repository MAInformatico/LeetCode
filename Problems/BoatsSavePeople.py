class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        result, begin = 0, 0
        end = len(people) - 1
                
        while begin <= end:
            
            if (people[begin] + people[end]) <= limit:                  
                result += 1
                begin += 1
                end -= 1

            else:
                end -= 1
                result += 1
        
        if begin == end:
            result += 1
        
        return result
