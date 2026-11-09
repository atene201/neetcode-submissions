class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # find the two greatest values in heights
        # reference there indicies 
        # indicies are used to calculate the width
        # height is min(the greatest values in heights)



        left = 0
        right = len(heights)-1

        areas = []

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = height * width
            areas.append(area)

            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                left += 1
                right -= 1

        return max(areas)





