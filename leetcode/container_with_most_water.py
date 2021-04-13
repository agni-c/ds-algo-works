from typing import List


def maxAreaBrute(self, height: List[int]) -> int:
    res = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            area = (j - i) * min(height[i], height[j])  # j,i => distence of each wall height[l],height[r]=>height
            res = max(res, area)
    return res


def maxArea(self, height: List[int]) -> int:
    res = 0
    l, r = 0, len(height) - 1
    while l < r:
        maxArea = (r - l) * min(height[l], height[r])
        res = max(res, maxArea)

        # maximize the polls on both

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return res
