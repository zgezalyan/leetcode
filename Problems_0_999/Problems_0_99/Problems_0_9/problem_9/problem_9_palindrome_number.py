class Solution:
    def isPalindrome_simple(self, x: int) -> bool:
        return True if str(x) == str(x)[::-1] else False

    def isPalindrome_optimized(self, x: int) -> bool:
        # Reject negative numbers and numbers ending with 0 (except 0 itself).
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Reverse only the second half of the number.
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + (x % 10)
            x //= 10

        # For odd length numbers, drop the middle digit from reversed_half.
        return x == reversed_half or x == reversed_half // 10
    
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        buf = 0
        while x > buf:
            buf = buf * 10 + (x % 10)
            x = x // 10
        return x == buf or x == buf // 10
