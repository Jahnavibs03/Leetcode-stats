# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        n = 0
        r = rand7() + rand7()
        
        while r > 0:
            n += rand7()
            r -= 1
        n = n % 10
        if n == 0:
            n = 10
        return n

        