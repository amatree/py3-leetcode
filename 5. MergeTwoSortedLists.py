# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __len__(self):
        if self.next is not None and len(self.next) >= 0:
            return 1 + len(self.next)
        return 0
    
    def __iter__(self):
        self._count = 0
        return self
    
    def __next__(self):
        if self._count <= len(self):
            self._count += 1
            return self.__str__()[self._count - 1]
        raise StopIteration
        
    def __str__(self):
        return str(self.val) + (self.next.__str__() if self.next != None else "")
    
class Solution(object):
    def listToListNode(self, list):
        ret = ListNode(list[0])
        tmp = ret
        list_iter = iter(list[1:])
        for i in list:
            n = next(list_iter, None)
            if n is not None:
                tmp.next = ListNode(n)
                tmp = tmp.next
                
        return ret
    
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if len(list1) == 0 or list1 is None: return list2 
        if len(list2) == 0 or list2 is None: return list1
        if len(list1) == len(list2) == 0: return []
        
        return sorted([*list1, *list2])
    
    def mergeTwoListNodes(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if len(list1) == 0 or list1 is None: return list2 
        if len(list2) == 0 or list2 is None: return list1
        if len(list1) == len(list2) == 0: return []
        
        return sorted([*list1, *list2])
            


list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))

s = Solution()

r = s.mergeTwoLists([1,2,4], [1,3,4])
d = s.mergeTwoListNodes(list1, list2)
print(d.__str__())
