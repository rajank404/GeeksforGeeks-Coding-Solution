class Solution:
    def countFreq(self, nums, target):
        # code here
        # temp = {}
        # for i in arr:
        #     if i not in temp:
        #         temp[i] = 1
        #     else:
        #         temp[i] += 1
        # for i,j in temp.items():
        #     if i == target:
        #         return j
        # return 0
        
        
        def firstOccurance(nums,target):
            first = -1
            l = 0
            h = len(nums) - 1
            while l <= h:
                mid = l + (h-l)//2
                if nums[mid] == target:
                    first = mid
                    h = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    h = mid - 1
            return first

        def lastOccurance(nums,target):
            last = -1
            l = 0
            h = len(nums) - 1

            while l <= h:
                mid = l + (h-l)//2
                if nums[mid] == target:
                    last = mid
                    l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    h = mid - 1
            return last

        first = firstOccurance(nums,target)
        last = lastOccurance(nums,target)
        if first == -1:
            return 0
        result = (last-first) + 1
        return result
        
        