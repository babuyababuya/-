# nums = [64, 34, 25, 12, 22, 11, 90]   m=7

def bubble(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


def test_bubble():
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    bubble(arr1)
    assert arr1 == [11, 12, 22, 25, 34, 64, 90], f"断言失败，实际返回{arr1}"

    print("All test passed")


test_bubble()
