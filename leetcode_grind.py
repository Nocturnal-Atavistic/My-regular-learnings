
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

# Below code worked for all the cases, even where there was substraction needed in the Roman

class Solution(object):
    def romanToInt(self, s):
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        sum = 0
        for i in range(len(s)-1):
            if translations[s[i]] < translations[s[i+1]]: # checking if the next roman numeral is bigger than the previous one, if yes then the deduction is to be done.
                sum -= translations[s[i]]
            else:
                sum += translations[s[i]]
        sum += translations[s[-1]] # for adding the last diggit into the sum

        return sum 


# Counting the word length from the last. "hello world", "hello World    " Now you look closely 2nd one is bit tough to get:

# my this code worked for 2 cases where last word was not the space:
class Solution(object):
    def lengthOfLastWord(self, s):
        count = 0
        for i in s[::-1]:
            if i == " ":
                break
            else: 
                count += 1

        return count      









