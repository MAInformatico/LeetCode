class Solution:
    def candy(self, ratings: List[int]) -> int:
        queue, length = deque(), len(ratings)

        ratings.append(float('inf')) 

        queue.extend(i for i in range(length) if ratings[i - 1] >= ratings[i] <= ratings[i + 1])

        candy, lv = [None] * length, 1

        while queue:
            for _ in range(len(queue)):
                i = queue.popleft()
                if 0 <= i < length:
                    candy[i] = lv
                    if ratings[i - 1] > ratings[i]: queue.append(i - 1)
                    if ratings[i + 1] > ratings[i]: queue.append(i + 1)
            lv += 1

        return sum(candy)
