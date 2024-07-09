# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
# 解释：需要合并 [1,2,3] 和 [2,5,6] 。
# 合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
# [124000] [345] [123445]
# [345000] [123] [345]
from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    while m > 0 and n > 0:
        if nums1[m-1] < nums2[n-1]:
            nums1[m-1+n] = nums2[n-1]
            n -= 1
        else:
            nums1[m-1+n] = nums1[m-1]
            m -= 1
    if m == 0 and n > 0:
        nums1[:n] = nums2[:n]


class Solution:
    pass


def test_merge():
    nums1 = [2, 4, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 4]
    n = 2
    merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 4, 4, 6, 0], f"Expected [1, 2, 4, 4, 6, 0] actual is{nums1}"
    print("All test cases passed.")


test_merge()
