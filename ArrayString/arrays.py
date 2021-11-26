'''Remove Ocurrance of element
    eg. Input: nums = [3,2,2,3], val = 3
        Output: 2, nums = [2,2,_,_]
        Explanation: Your function should return k = 2, with the first two elements of nums being 2.
        It does not matter what you leave beyond the returned k (hence they are underscores).
'''
def removeElement(self, nums, val: int) -> int:
        
        i = 0 
        
        for num in nums:
            if num != val:
                nums[i]=num
                i +=1
        return i

'''Maximum concecutive one'''
def findMaxConsecutiveOnes(self, nums) -> int:
        if not nums:
            return []
        ans = 0
        sum = 0

        for num in nums:
            
            if num == 0:
                sum = 0
                
            else:
                
                sum += num
                ans = max(ans, sum)

        return ans
'''remove duplicates on sortedd array'''
def removeDuplicates(self, nums) -> int:
    if not nums:
        return []
        
    i = 0 
        
    for num in nums : 
        if i < 1 or num  > nums[i-1]:
            nums[i]=num
            i +=1
    return i


'''Leetcode question find the pivot index .
    Pivot Index - The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal 
    to the sum of all the numbers strictly to the index's right

    Time : O(n)
    Space : O(1)

    Input : nums = [1,7,3,6,5,6]
    Output: 3

'''

def pivotIndex(self, nums) -> int:

    if not nums :
        return []

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

        EXAMPLE :
        Input: nums = [3,6,1,0]
        Output: 1
        Explanation: 6 is the largest integer.
        For every other number in the array x, 6 is at least twice as big as x.
        The index of value 6 is 1, so we return 1.
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
'''
    Diagonal Traversal 2-d array 
    we are going to divide the array in diagonals 
    look at the array below:

    8  9  11 14
    16 21 20 24
    31 13 40 42
    52 70 30 34

    from this array we first need to determine the number of diagonal we are going to have and they will be held in a list.
    This can be done by : number of rows + number of columns -1
    For our case we have 4 rows + 4 cols -1 = 7

    this diagonals are 7. 
    []
    []
    []
    []
    []
    []
    []

    so how do we know which value goes into which diagonal?
    to add into our diagonal we are going to add the i index to the j index of the array.
    i.e:
    
    8 from the array above is in position (0,0). so we add 0 + 0 = 0 
    thus we add it to the 0 diagonal.
    9 from the array above is in position (0,1). so we add 0 + 1 = 1
    thus we add it to the 0 diagonal.
    
    [8]
    [9]
    []
    []
    []
    []
    []
    and so on.
    we then construst our final results by adding the diagonal elements to the final list.
    but there are diagonals that need to be added in reverse. 
    To handle that we will add the diagonals the have even length as they are,
    but for the odd we will add in reverse 

'''
def findDiagonalOrder(self, mat) :
        if not mat or not mat[0]:#base case, check if matrix is empty or if the we have 0 columns 
            return []

        num_rows, num_cols = len(mat),len(mat[0])
        diagonals = [[]for _ in range(num_rows + num_cols - 1)]#lost comprehensions and create a new list 
        
        for i in range(num_rows):
            for j in range(num_cols):
                diagonals[i+j].append(mat[i][j])
        res = diagonals[0] # we take care of the first 
        
        for x in range(1, len(diagonals)):
            if x % 2 == 1:
                res.extend(diagonals[x])# we do this so tht we add just the elements of the list not the whole list
            else: 
                res.extend(diagonals[x][::-1])
        return res
'''
    Print matrix in spiral order:
    the idea is to read elements from the given matrix and print the matrix in spiral order.
    Four loops are used to maintain the spiral order , each or the top,right bottom,and left coners of the matrix

'''
def spiralOrder(self, matrix) :
        #base case 
        if not matrix or not len(matrix):
            return 
        
        top= 0 #top of row
        bottom = len(matrix)-1 # bottom of row
        right = len(matrix[0]) - 1 # end of column 
        left = 0 # start of column 
        res = []
        
        while True:
            if left > right :
                break
            
            #print top row
            for i in range (left,right+1):
                print(matrix[top][i],end='')
                res.append(matrix[top][i])
            top = top +1 # move top down
            
            if top > bottom:
                break
            
            #print right column
            for i in range(top,bottom+1):
                print (matrix[i][right],end = '')
                res.append(matrix[i][right])
            right = right -1
            
            if left > right : 
                break
            
            # print bottom row
            for i in range(right, left -1, -1):
                print(matrix[bottom][i],end = '')
                res.append(matrix[bottom][i])
            bottom = bottom -1 
            
            if top > bottom:
                break
            
            # print left column 
            for i in range(bottom,top -1,-1):
                print(matrix[i][left], end = '')
                res.append(matrix[i][left])
            left = left + 1
            # printSpiral(mat, top, bottom, left, right) recursion
        return res
'''
    Given an integer numRows, return the first numRows of Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
'''
def generate(self, numRows: int):
        res = [[1]]
        
        for i in range(numRows - 1):
            temp = [0]+res[-1]+[0]
            row = []
            
            for j in range(len(res[-1])+1):
                row.append(temp[j]+temp[j+1])
            res.append(row)
            
        return res 

'''
ALTERNATIVE 
    def PascalTriangle(n):
   trow = [1]
   y = [0]
   for x in range(n):
      print(trow)
      trow=[left+right for left,right in zip(trow+y, y+trow)]
   return n>=1
'''

'''  Minimum Size Subarray Sum
    microsoft 

'''
def minSubArrayLen(self, target: int, nums) -> int:
        ans = inf
        sum = 0
        j = 0

        for i, num in enumerate(nums):
            sum += num
            while sum >= target:
                ans = min(ans, i - j + 1)
                sum -= nums[j]
                j += 1

        return ans if ans != inf else 0

'''Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized.
     Return the maximized sum.
     
     '''
def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0 
        sum = 0 
        
        while i < len(nums) - 1:
            sum += nums[i]
            i+=2
        return sum
'''
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    Note that you must do this in-place without making a copy of the array.
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]'''
def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0 
        
        for num in nums:
            if num !=0:
                nums[j]=num
                j+=1
        for i in range(j,len(nums)):
            nums[i]=0

#################################################################################################################################################################
# STRING LEETCODE QUESTIONS 

'''ADD BINARY 
    Given two binary strings a and b, return their sum as a binary string.

    BINARY ADDITION EXAMPLE : remember 1+1 is 0 in binary and you carry 1 
    1 1
    + 1
    ----
    100
    ----
'''
def addBinary(self, a: str, b: str) -> str:

    s = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
            
        if i >= 0:
            carry += int(a[i])
            i -= 1
        if j >= 0:
                
            carry += int(b[j])
            j -= 1
        s.append(str(carry % 2))
        carry //= 2

    return ''.join(s[::-1])

'''
    Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
    time: O((n *m))
'''
def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0 
        for i in range(len(haystack) + 1 - len(needle)): # to avoid starting at every position including the last
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1

'''Longest common prefex'''
def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ''

        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != strs[0][i]:
                    return strs[0][:i]

        return strs[0]

'''REverse a string '''
def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1 
        
        while l < r:
            #swap the elements
            s[l],s[r] = s[r],s[l]
            
            l +=1
            r -= 1

'''add minimum maximum
    Time: O(n) \to O(n\log n)O(n)→O(nlogn)$
    Space: O(n) \to O(1)O(n)→O(1)
'''
def arrayPairSum(self, nums) -> int:
    return sum(sorted(nums)[::2])
'''
def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0 
        sum = 0 
        
        while i < len(nums) - 1:
            sum += nums[i]
            i+=2
        return sum
'''
''' 
    TWO SUM I
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.
'''
def twoSum(self, numbers, target: int) :
        
        numToIndex = {} #val :index

        for i, num in enumerate(numbers):
            
            if target - num in numToIndex:
                
                return numToIndex[target - num], i
            
            numToIndex[num] = i
'''
    TWO SUM II - SORTED ARRAY 
    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

    Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

    The tests are generated such that there is exactly one solution. You may not use the same element twice.
'''
def twoSum(self, numbers, target: int) :
        
        l = 0 
        r = len(numbers) - 1
        
        while l < r:
            sum = numbers[l]+ numbers[r]
            if sum == target:
                return [l+1,r+1]
            if sum < target:
                l+=1
            else:
                r-=1
''' Rotate array:
    Given an array, rotate the array to the right by k steps, where k is non-negative.

    Aproach : 
        we will first rotate the whole list
        then split the listand roate each positions respectively 

'''
def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
#rotation helper
def reverse(self, nums: List[int], l: int, r: int) -> None:
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
'''Reverse Words in a String :
    Input: s = "the sky is blue"
    Output: "blue is sky the"

'''
def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))

'''
    Reverse Words in a String III:
    Given a string s, reverse the order of characters in each word within a sentence 
    while still preserving whitespace and initial word order.
    example:
    Input: s = "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"
'''
def reverseWords(self, s: str) -> str:
        return " ".join([word[::-1] for word in s.split()])