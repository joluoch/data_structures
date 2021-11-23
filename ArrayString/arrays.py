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

#################################################################################################################################################################
# STRING LEETCODE QUESTIONS 
