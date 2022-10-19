class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_ps = "([{"
        close_ps = ")]}"
        order = []
        
        for p in s:
            o = open_ps.find(p)
            c = close_ps.find(p)
            
            if o != -1:
                order.append(o)
            
            if c != -1:
                if len(order) == 0:
                    return False
                if c != order[-1]:
                    return False
                order.pop()
        
        return not order