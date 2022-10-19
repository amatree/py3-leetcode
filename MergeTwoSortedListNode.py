# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1.val == None and list2.val == None: return []
        if list1.val == None: return list2
        if list2.val == None: return list1
        if list1.val > list2.val:
            list1, list2 = list2, list1
        
        result = [list1.val]
        _next_1 = list1.next
        _next_2 = list2
                
        while True:
            _curr_node = None
            if _next_1 is not None and _next_2 is not None:
                if _next_1.val <= _next_2.val:
                    result.append(_next_1.val)
                    _next_1 = _next_1.next
                else:
                    result.append(_next_2.val)
                    _next_2 = _next_2.next
                
            elif _next_1 is None: 
                while _next_2 is not None:
                    result.append(_next_2.val)
                    _next_2 = _next_2.next
                break
                    
            elif _next_2 is None:
                while _next_1 is not None:
                    result.append(_next_1.val)
                    _next_1 = _next_1.next
                break
            else:
                break
        
        return result
        
s = Solution()

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

r = s.mergeTwoLists(list1, list2)

s = r
st = ""
while s is not None:
    st += str(s.val) + " + "
    s = s.next

print(st)