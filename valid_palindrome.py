
class Solution:

    def isPalindrome(self, s: str) -> bool:
        s = [character.lower() for character in s if character.isalnum()]

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama") is True)
    print(solution.isPalindrome("race a car") is False)
    print(solution.isPalindrome(" ") is True)

