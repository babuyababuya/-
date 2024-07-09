# 输入：nums = [0,0,1,1,1,2,2,3,3,4]  n =10
# 输出：5, nums = [0,1,2,3,4]
# 解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


def test_remove_duplicates():
    sol = Solution()

    # Test Case 1
    nums1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected_len1 = 5
    expected_nums1 = [0, 1, 2, 3, 4]
    result1 = sol.removeDuplicates(nums1)
    assert result1 == expected_len1, f"Expected length {expected_len1}, but got {result1}"
    assert nums1[:result1] == expected_nums1, f"Expected {expected_nums1}, but got {nums1[:result1]}"

    # Test Case 2
    nums2 = [1, 1, 2]
    expected_len2 = 2
    expected_nums2 = [1, 2]
    result2 = sol.removeDuplicates(nums2)
    assert result2 == expected_len2, f"Expected length {expected_len2}, but got {result2}"
    assert nums2[:result2] == expected_nums2, f"Expected {expected_nums2}, but got {nums2[:result2]}"

    print("All test cases passed.")


# Run the test cases
test_remove_duplicates()
