class Solution:
    def permute_unique(self,nums):
        res = []

        def solve(idx):
            if idx == len(nums):
                res.append(nums[:])
                return
            used = set()

            for i in range(idx, len(nums)):
                if nums[i] in used :
                    continue
                used.add(nums[i])

                nums[idx], nums[i] = nums[i], nums[idx]

                solve(idx + 1)

                nums[idx], nums[i] = nums[i], nums[idx]


        solve(0)
        return res


nums = list(map(int, input("Enter a number:").split()))

obj = Solution()
print(obj.permute_unique(nums))