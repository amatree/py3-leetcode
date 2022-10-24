class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            for i, v in enumerate(nums2):
                nums1[i] = v
            return
            
        j = 0
        curr = nums2[j]
        for i in range(m + n):
            if j == n:
                break
            if i < n:
                # print(f"{curr} vs {nums1[i+1]}")
                if nums1[i] <= curr:
                    while i < m and nums1[i] < curr:
                        # if nums1[i+1] == 0: break
                        i += 1
                    # if nums1[i] == 0: nums1.insert(i, curr)
                    # else: nums1.insert(i+1, curr)
                    nums1.insert(i, curr)
                    # print(f"*inserted {curr} to nums1[{i}]") 
                else:
                    nums1.insert(i+1, curr)
                    # print(f"**inserted {curr} to nums1[{i+1}]")
                nums1.pop()
                if j < n: 
                    j += 1
                    curr = nums2[j]
            if i+1 >= m:
                for i, v in enumerate(nums2, start=j):
                    nums1[i+1] = v
                return
            if i >= n:
                nums1[-1] = nums2[-1]
                break
                
s = Solution()

nums1 = [1,2,3,0,0,0]
nums2 = [4,5,6]

print(f"Merging \n'nums1': {nums1}\n'nums2': {nums2}")

s.merge(nums1, len(nums1) - nums1.count(0), nums2, len(nums2))

print(f"--> {nums1}")