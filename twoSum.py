class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        if len(num) < 2:
            return
        seen = set()
        for elem in num:
            temp = target-elem
            if temp not in seen:
                seen.add(elem)
            else:
                answer1 = num.index(temp)+1
                if temp == elem:
                    num[answer1-1] = elem+1
                
                answer2 = num.index(elem)+1
                return answer1, answer2
                
