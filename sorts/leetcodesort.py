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

'''search a 2d matrix#'''
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    ROW,COL = len(matrix),len(matrix[0])
        
        #first binary to find the correct row
        
    top_row, bot_row = 0,ROW-1
        
    while top_row < bot_row :
        mid_row = (top_row+bot_row)//2
            
        if target > matrix[mid_row][-1]: # target is larger than largest val in row
                top_row = mid_row +1
        elif target < matrix[mid_row][0]:
                bot_row = mid_row - 1
        else:
            break 
            #our condition might be in valid so 
            
    if not top_row <= bot_row:
        return False 
    mid_row = (top_row + bot_row) //2
        
    l,r = 0, COL -1
        
    while l<= r:
        mid_col= (l+r)//2
            
        if target > matrix[mid_row][mid_col]:
            l = mid_col+1
        elif target < matrix[mid_row][mid_col]:
            r = mid_col -1
        else:
            return True
    return False
'''search 2 d matrix 2'''
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix :
            return False
        row,col = len(matrix),len(matrix[0])
        r = 0
        c = col - 1
        
        while r < row and c >= 0:
            if target == matrix[r][c]:
                return True
            if target< matrix[r][c]:
                c-=1
            else:
                r+=1
        return False

'''median oof two sorted arrays
'''

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    n1 = len(nums1)
    n2 = len(nums2)

    if n1 > n2:
      return self.findMedianSortedArrays(nums2, nums1)

    l = 0
    r = n1

    while l <= r:
      partition1 = l + (r - l) // 2
      partition2 = (n1 + n2 + 1) // 2 - partition1
      maxLeft1 = -2**31 if partition1 == 0 else nums1[partition1 - 1]
      maxLeft2 = -2**31 if partition2 == 0 else nums2[partition2 - 1]
      minRight1 = 2**31 - 1 if partition1 == n1 else nums1[partition1]
      minRight2 = 2**31 - 1 if partition2 == n2 else nums2[partition2]
      if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
        return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) * 0.5 if (n1 + n2) % 2 == 0 else max(maxLeft1, maxLeft2)
      elif maxLeft1 > minRight2:
        r = partition1 - 1
      else:
        l = partition1 + 1
