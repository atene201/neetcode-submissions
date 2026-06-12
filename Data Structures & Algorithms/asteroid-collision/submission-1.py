class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # abs val = size
        # sign = direction (+ : right, - : left)
        # each one moves at the same speed

        # if they meet, smaller one explodes
        # same size : both explode
        # two moving in the same dir will never meet

        final_state = []

        for asteroid in asteroids:
            while final_state and asteroid < 0 and final_state[-1] > 0:
                # find which asteroid to explode
                diff = asteroid + final_state[-1]

                if diff < 0:
                    final_state.pop()
                elif diff > 0:
                    asteroid = 0
                else:
                    asteroid = 0
                    final_state.pop()
            if asteroid:
                final_state.append(asteroid)
        return final_state