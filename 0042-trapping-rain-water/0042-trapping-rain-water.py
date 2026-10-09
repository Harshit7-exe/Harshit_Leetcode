class Solution:
    def trap(self, height: list[int]) -> int:
        left_height = 0
        right_height = len(height) - 1
        left_max = 0
        right_max = 0
        water = 0
        while right_height > left_height:
            if height[left_height] < height[right_height]:
                if height[left_height] > left_max:
                    left_max = height[left_height]
                else:
                    water += left_max - height[left_height]
                left_height += 1
            else:
                if height[right_height] > right_max:
                    right_max = height[right_height]
                else:
                    water += right_max - height[right_height]
                right_height -= 1
        return water
