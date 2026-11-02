class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def getNext(nums):
            total=0
            while nums>0:
                digit=nums%10
                total+=digit*digit
                nums//=10
            return total
        slow=n
        fast=getNext(n)
        while fast!=1 and slow!=fast:
            slow=getNext(slow)
            fast=getNext(getNext(fast))
        return fast==1