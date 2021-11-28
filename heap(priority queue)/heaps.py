
''''''
def findKthLargest(self, nums: List[int], k: int) -> int:
    # we are going to use a heapify
    # we will conver t the array into a max heap then pop the elements k times and return 
    # we will use the quick select
        nums.sort()
        return nums[len(nums)-k]