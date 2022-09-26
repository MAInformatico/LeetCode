class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        atomics = {x: {x} for x in string.ascii_lowercase}
        for x, symbol, _, y in equations:
            if symbol == "=":
                atomics[x] |= atomics[y]
                for i in atomics[x]:
                    atomics[i] = atomics[x]
        return all(atomics[x] is not atomics[y] for x, symbol, _, y in equations if symbol == "!")
