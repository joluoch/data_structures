'''Leetcode question fine the pivot index .
    Pivot Index - The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal 
    to the sum of all the numbers strictly to the index's right

    Time : O(n)
    Space : O(1)

    Input : nums = [1,7,3,6,5,6]
    Output: 3

'''

def pivotIndex(self, nums) -> int:

    add = sum(nums)
    leftnums = 0 
        
    for i, num in enumerate(nums): #looping through every index and value
        if leftnums  == add - leftnums - num:
            return i
        leftnums += num
    return -1

'''
    You are given an integer array nums where the largest integer is unique.

    Determine whether the largest element in the array is at least twice as much as every other number in the array. 
    If it is, return the index of the largest element, or return -1 otherwise.

    approach : 
        Find the max in the original list 
        make a new array with the other values 
        find the max in new array
        if original max is >= to new_array * 2 then return original max index else return -1
'''
def dominantIndex(self, nums) -> int:
        f  = max(nums)
        rs = nums.index(f)
        new_array = []
        new_max = 0
        
        for i in nums:
            if i != f:
                new_array.append(i)
        if len(new_array) != 0:
            new_max = max(new_array)
        if f >= 2 * new_max:
            return rs
        else:
            return -1

'''
    You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
    The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits.

    cases to watch for : [9,9,9,9] and [1,2,3,9]

    time : O(n)
    space : O(1)

'''
def plusOne(self, digits) :
        digits = digits[::-1] # reverse the array
        carry = 1
        index = 0 
        
        while carry:
            if index < len(digits):#edgecase
                if digits[index] == 9: # having 9 at the end
                    digits [index] = 0 # change it to 0
                else:
                    digits[index] += 1
                    carry = 0
            else:
                digits.append(1)
                carry = 0
            index += 1
        return digits[::-1]
