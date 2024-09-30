class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Solution 1
        # pointerLeft = 0
        # pointerRight = len(height) - 1

        # areas = []

        # while pointerLeft < pointerRight:
        #     area = min(height[pointerRight], height[pointerLeft]) * (pointerRight - pointerLeft)
        #     areas.append(area)
        #     if height[pointerRight] < height[pointerLeft]:
        #         pointerRight -= 1
        #     else:
        #         pointerLeft += 1

        # return max(areas)

        # Solution 2
        pointerLeft = 0
        pointerRight = len(height) - 1

        maxArea = 0

        while pointerLeft < pointerRight:
            area = min(height[pointerRight], height[pointerLeft]) * (pointerRight - pointerLeft)
            if area > maxArea:
                maxArea = area
            if height[pointerRight] < height[pointerLeft]:
                pointerRight -= 1
            else:
                pointerLeft += 1

        return maxArea
