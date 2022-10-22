class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0: 
            nums1.pop(0)
            nums1.extend(nums2)
            return
        if n == 0:
            return
        
        for i in range(m + n):
            if i < n:
                print(nums2[i], " vs ", nums1[i])
                if nums1[i] <= nums2[i]:
                    if nums1[i+1] >= nums2[i]:
                        nums1.insert(i+1, nums2[i])
                        nums1.pop()
            else:
                break
        
        
                
s = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
s.merge(nums1, 3, nums2, 3)

print(nums1)