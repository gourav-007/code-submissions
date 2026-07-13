class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        n = len(words)

        for i in range(0,n):
            for j in range(0,n):
                if words[i] in words[j] and i!=j:
                    ans.append(words[i])
                    break
        return ans