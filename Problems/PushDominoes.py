class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        aux = ''
        
        while dominoes != aux:
            aux = dominoes
            dominoes = dominoes.replace('R.L', 'xxx')
            dominoes = dominoes.replace('R.', 'RR')
            dominoes = dominoes.replace('.L', 'LL')
            
        return dominoes.replace('xxx', 'R.L')
