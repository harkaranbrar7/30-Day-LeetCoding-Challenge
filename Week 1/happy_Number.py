'''Happy Number
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

'''
class Solution1:
    seen = set()
    def isHappy(self, n: int) -> bool:
        if n in Solution1.seen:
            # clear the cache for next try
            Solution1.seen.clear()
            return False
        Solution1.seen.add(n)

        s = sum(l*l for l in map(int,str(n)))

        if s == 1:
            # clear the cache for next try
            Solution1.seen.clear()
            return True

        return self.isHappy(s)

class Solution2:
    def isHappy(self, n: int) -> bool:
        """
        :type n: int
        :rtype: bool
        """
        while n != 1 and n != 4:
            _sum = 0
            while n :
                _sum += (n % 10) * (n % 10)
                n //= 10
            n = _sum

        return n == 1

class Solution3:
    def isHappy(self, n):
        s = set()
        while n != 1:
            if n in s: return False
            s.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        else:
            return True

class Solution4:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while n != 1:
            if n in s: return False
            s.add(n)

            _sum = 0
            while n:
                _sum += (n % 10) ** 2
                n //= 10
            n = _sum

        return n == 1

class Solution5:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while n:
            if 1 in s:
                return True
            if n in s:
                return False
            s.add(n)
            _sum = 0
            while n:
                _sum += (n%10)**2 #leave unit digit
                n //= 10 #remvoe unit digit 
            n = _sum

class Solution6:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n != 1 and n != 4:
            _sum = 0
            while n :
                _sum += (n % 10) * (n % 10)
                n //= 10
            n = _sum

        return n == 1