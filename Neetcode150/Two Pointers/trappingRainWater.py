class Solution:
    def trap(self, height: list[int]) -> int:

        # Solution 1

        pointerLeft = 0
        pointerRight = height.index(max(height))

        sumOfWater = 0

        for i in range(len(height)):
            if height[pointerLeft] < height[i]:
                pointerLeft = i
            if pointerRight < i:
                pointerRight = height.index(max(height[i::]))
            sumOfWater += (min(height[pointerLeft], height[pointerRight]) - height[i])

        return sumOfWater

        # Solution 2

        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        sumOfWater = 0

        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                sumOfWater += max(0, maxLeft - height[left])
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                sumOfWater += max(0, maxRight - height[right])

        return sumOfWater
