class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = -1 
        for index in range(len(arr)-1, -1, -1):
            aux = arr[index]
            arr[index] = current_max
            if current_max < aux:
                current_max = aux

        return arr
