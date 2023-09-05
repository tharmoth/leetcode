class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cache = {}
        for s_char, t_char in zip(s, t):
            cache[s_char] = cache.get(s_char, 0) + 1
            cache[t_char] = cache.get(t_char, 0) - 1

        return not any(cache.values())


if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram") is True)
    print(solution.isAnagram("rat", "car") is False)
