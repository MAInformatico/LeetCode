class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []
        for i in range(len(accounts)):
            aux = sum(accounts[i])
            wealth.append(aux)
        
        return max(wealth)
