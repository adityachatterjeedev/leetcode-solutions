# Last updated: 2/22/2026, 7:57:20 PM
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count_t = 0
        count_f = 0
        res = 0
        left = 0
        for right in range(len(answerKey)):
            if answerKey[right] == 'T':
                count_t += 1
            else:
                count_f += 1

            while min(count_t, count_f) > k:
                if answerKey[left] == 'T':
                    count_t -= 1
                else:
                    count_f -= 1
                left += 1

            res = max(res, right - left + 1)

        return res