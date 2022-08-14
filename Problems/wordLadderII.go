func differencesChar(x, y string ) int {
    result := 0
    for iter, _ := range x{
        if x[iter] != y[iter]{
            result++;
        }
    }
    return result
}

func findLadders(beginWord string, endWord string, wordList []string) [][]string {
    hashMap := map[string]int{beginWord:0} 
    q := make([]string, 0) 
    q = append(q, beginWord)
    for len(q) > 0 { 
        currentWord := q[0]
        q = q[1:] 
        for _, nextWord := range wordList { 
            if _, have := hashMap[nextWord]; !have && differencesChar(currentWord, nextWord) == 1 { 
                q = append(q, nextWord) 
                hashMap[nextWord] = hashMap[currentWord] + 1
            }
        }
    }
    
    result := [][]string{}
    if _, have := hashMap[endWord]; !have {
        return result
    }

    var dfs func(currentWord string, current []string) 
    dfs = func(currentWord string, current []string) {
        current = append(current, currentWord)
        if (hashMap[currentWord] == 1) { 
            current = append(current, beginWord) 
            aux := current
            for i, j := 0, len(aux)-1; i < j; i, j = i + 1, j - 1 {
                aux[i], aux[j] = aux[j], aux[i]
            }
            result = append(result, aux)
            current = current[:len(current)-2]
            return;
        }           
        for _, nextWord := range wordList {
            if _, have := hashMap[nextWord]; have && differencesChar(currentWord, nextWord) == 1 && hashMap[currentWord] == hashMap[nextWord] + 1 {
                dfs(nextWord, current)
            }
        }        
        current = current[:len(current)-1]
    }
    dfs(endWord, []string{})
    
    return result
}
