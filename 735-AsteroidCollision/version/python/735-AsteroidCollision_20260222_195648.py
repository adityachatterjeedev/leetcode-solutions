# Last updated: 2/22/2026, 7:56:48 PM
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        pos_a = []
        neg_a = []

        for a in asteroids:
            if a < 0:
                destroy = False
                while len(pos_a) > 0:
                    if abs(a) > pos_a[-1]:
                        pos_a.pop()
                    elif abs(a) == pos_a[-1]:
                        pos_a.pop()
                        destroy = True
                        break
                    else:
                        destroy = True
                        break
                if not destroy:
                    neg_a.append(a)

            else:
                pos_a.append(a)
        
        return neg_a + pos_a