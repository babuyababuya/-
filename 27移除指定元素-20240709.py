# 输入：nums = [0,1,2,2,3,0,4,2], val = 2
# 输出：5, nums = [0,1,4,0,3,_,_,_]
# 解释：你的函数应该返回 k = 5，并且 nums 中的前五个元素为 0,0,1,3,4。
# n
# 双指针 快指针，慢指针
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        fast = slow = 0
        while fast < n:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


def test_remove_element():
    sol = Solution()

    # Test Case 1
    nums1 = [0, 1, 2, 2, 3, 0, 4, 2]
    val1 = 2
    expected_len1 = 5
    expected_nums1 = [0, 1, 3, 0, 4]
    result1 = sol.removeElement(nums1, val1)
    assert result1 == expected_len1, f"Expected length {expected_len1}, but got {result1}"
    assert nums1[:result1] == expected_nums1, f"Expected {expected_nums1}, but got {nums1[:result1]}"

    # Test Case 2
    nums2 = [3, 2, 2, 3]
    val2 = 3
    expected_len2 = 2
    expected_nums2 = [2, 2]
    result2 = sol.removeElement(nums2, val2)
    assert result2 == expected_len2, f"Expected length {expected_len2}, but got {result2}"
    assert nums2[:result2] == expected_nums2, f"Expected {expected_nums2}, but got {nums2[:result2]}"

    print("All test cases passed.")


# Run the test cases
test_remove_element()