class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 1q: will the res array hold the number of days
        # before a warmer temp?

        # [ 10, 9, 8, 7, 11] 
        # res = [0, 0, 0, 1, 0]

        # use a monotonic stack to track the prev temp w index

        res = [0] * len(temperatures)
        stack = [] # hold (temp, index) inside an array

        for i, tmp in enumerate(temperatures):
            while stack and tmp > stack[-1][0]:
                stack_temp, stack_idx = stack.pop()
                res[stack_idx] = i - stack_idx
            stack.append((tmp, i))
        return res