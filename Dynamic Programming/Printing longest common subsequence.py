class solution(object):
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.l1 = len(str1)
        self.l2 = len(str2)
        self.memo = [[0 for i in range(self.l2+1)] for j in range(self.l1+1)]
        self.__rec_with_memo(self.l1, self.l2)

    def __rec_with_memo(self, l1, l2):
            if l1 == 0 or l2 == 0:
                return 0
            
            if self.memo[l1][l2] != 0:
                return self.memo[l1][l2]
            
            if self.str1[l1-1] == self.str2[l2-1]:
                self.memo[l1][l2] = 1 + self.__rec_with_memo(l1-1, l2-1)
            else:
                self.memo[l1][l2] = max(self.__rec_with_memo(l1-1, l2), self.__rec_with_memo(l1, l2-1))
                
            return self.memo[l1][l2]  
    def get_substring(self, i, j):
        substring = ""
        while i > 0 and j > 0:
            if self.str1[i-1] == self.str2[j-1]:
                substring += self.str1[i-1]
                i -= 1
                j -= 1
            else:
                if self.memo[i-1][j] > self.memo[i][j-1]:
                    i -= 1
                else:
                    j -= 1
        return substring[::-1]        
                
        


s1 = "abcdgh"
s2 = "abedfhr"
b=solution(s1,s2)
print(b.get_substring(len(s1),len(s2)))
