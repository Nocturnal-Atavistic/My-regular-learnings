
# Roman to number Problem, Below code worked for 2 cases ( "III" and "LVIII") but didn't worked for 3rd case ("MCMXCIV")
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

class Solution(object):
    def romanToInt(self, s):
        self.s = s
        sum = 0
        for i in self.s:
            if i == "I":
                sum = sum + I
            elif i == "V":
                sum = sum + V
            elif i == "X":
                sum = sum + X
            elif i == "L":
                sum = sum + L
            elif i == "C":
                sum = sum + C
            elif i == "D":
                sum = sum + D
            elif i == "M":
                sum = sum + M

        return sum
    
ans = Solution()
final = ans.romanToInt("III")
print(final)





