 def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0 
        r= len(nums)-1
        
        i =0 
        
        while i<=r:
            if nums[i] == 0:
                nums[i],nums[l] = nums[l],nums[i]
                i+=1
                l+=1
            elif nums[i]== 1:
            
                i +=1
            else:
                
                nums[i],nums[r] = nums [r],nums[i]
                r-=1


'''FInd minimum sorted array 1 
    using binary search tim = O(logn)
'''
def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) -1
        
        while l<r:
            m = (l+r) // 2 #find mid
            if nums[m] < nums[r]:
                r = m
            else:
                l = m+1
        
        return nums[l]

'''find min array 2 
    with duplicates 
    time = O(n)
'''
def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums)-1
        
        while l<r:
            m = (l+r) // 2
            if nums[m] == nums[r]:
                r-=1
            elif nums[m] < nums[r]:
                
                r = m
            else:
                l= m+1
        return nums[l]

'''search in a sorted array 
    time = O(logn) ->binary search 
'''
def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:  # nums[l..m] are sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:  # nums[m..n - 1] are sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1