# 123321 False
# 12321 True


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        if s == s[::-1]:
            return True
        else:
            return False


def test_is_palindrome():
    sol = Solution()

    # Test Case 1: Positive palindrome case
    x1 = 12321
    expected1 = True
    result1 = sol.isPalindrome(x1)
    assert result1 == expected1, f"Expected {expected1}, but got {result1}"

    # Test Case 2: Negative palindrome case
    x2 = 123321
    expected2 = True
    result2 = sol.isPalindrome(x2)
    assert result2 == expected2, f"Expected {expected2}, but got {result2}"

    # Test Case 3: Single digit
    x3 = 5
    expected3 = True
    result3 = sol.isPalindrome(x3)
    assert result3 == expected3, f"Expected {expected3}, but got {result3}"

    # Test Case 4: Negative number
    x4 = -121
    expected4 = False
    result4 = sol.isPalindrome(x4)
    assert result4 == expected4, f"Expected {expected4}, but got {result4}"

    # Test Case 5: Large palindrome number
    x5 = 12345678987654321
    expected5 = True
    result5 = sol.isPalindrome(x5)
    assert result5 == expected5, f"Expected {expected5}, but got {result5}"

    print("All test cases passed.")


# Run the test cases
test_is_palindrome()
