# Last updated: 2/22/2026, 7:47:46 PM
1class Solution:
2    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
3        stack = []
4
5        for asteroid in asteroids:
6            alive = True
7
8            while alive and asteroid < 0 and stack and stack[-1] > 0:
9                if stack[-1] < -asteroid:
10                    stack.pop()
11                elif stack[-1] == -asteroid:
12                    stack.pop()
13                    alive = False
14                else:
15                    alive = False
16
17            if alive:
18                stack.append(asteroid)
19
20        return stack