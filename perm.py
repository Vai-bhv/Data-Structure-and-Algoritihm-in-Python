# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Hello world")
class Solution(object):
   def nextPermutation(self, nums):
      found = False

      nums = nums.split()
      nums = [int(x) for x in nums if x != " "]
      i = len(nums)-2
      while i >=0:
         if (nums[i]) < (nums[i+1]):
            found =True
            break
         i-=1
      if not found:
         return "NEEXISTUJE"
      else:
         m = self.findMaxIndex(i+1,nums,nums[i])
         nums[i],nums[m] = nums[m],nums[i]
         nums[i+1:] = nums[i+1:][::-1]
      nums = [str(x) for x in nums]
      return " ".join(nums)
   def findMaxIndex(self,index,a,curr):
      ans = -1
      index = 0
      for i in range(index,len(a)):
         if a[i]>curr:
            if ans == -1:
               ans = curr
               index = i
            else:
               ans = min(ans,a[i])
               index = i
      return index
n = int(input())
nn = input()
ob1 = Solution()
print(ob1.nextPermutation(nn))