'''best time to buy and sell stock'''
def maxProfit(self, prices: List[int]) -> int:
    l,r = 0,1 #left==buying right == selling
    maxP = 0
        
    while r < len(prices):
            #profitability 
        if prices[l] < prices [r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP,profit)
        else:
            l=r
        r+=1
    return maxP

'''maximum subarry'''
def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        
        for i , num in enumerate(nums):
            if i>0 and dp[i-1]>0:
                dp[i] = dp[i-1]+num
            else:
                dp[i] = num
        return max(dp)

'''longest increaing subsequence '''

def lengthOfLIS(self, nums: List[int]) -> int:
        
    LIS = [1] * len(nums)
        
    for i in range(len(nums)-1,-1,-1):
        for j in range(i+1,len(nums)):
            if nums[i]<nums[j]:
                LIS[i] = max(LIS[i],1+LIS[j])
    return max(LIS)