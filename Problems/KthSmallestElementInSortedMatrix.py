array = []
        for i in range(len(matrix)):
            array = array + matrix[i]
        array.sort()
        return array[k-1]
