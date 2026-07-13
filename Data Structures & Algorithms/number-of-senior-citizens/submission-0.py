class Solution:
    def countSeniors(self, details: List[str]) -> int:
        n = len(details)
        count=0

        for i in range(0,n):
            detail = details[i]

            if int(detail[11:13]) > 60:
                count+=1

        return count