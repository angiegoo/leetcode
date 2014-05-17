class Solution:
    # @return an integer
    def atoi(self, stri):
        answer = 0
        sign = 1
        i = 0
        if stri == '':
            return 0
        while stri[i] == ' ' and i < len(stri):
            i+=1
        if stri[i] == '+':
            sign = 1
            i+=1
        elif stri[i] == '-':
            sign = -1
            i+=1
        for j in range(i, len(stri)):
            if stri[j] in ['1','2','3','4','5','6','7','8','9','0']:
                answer = answer*10+int(stri[j])
            else:
                break
        answer = answer*sign
        if answer < -2147483648: 
            return -2147483648
        elif answer > 2147483647:
            return 2147483647
        else: return answer    
