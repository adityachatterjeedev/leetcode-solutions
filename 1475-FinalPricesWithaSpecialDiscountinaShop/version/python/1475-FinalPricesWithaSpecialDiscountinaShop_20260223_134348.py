# Last updated: 2/23/2026, 1:43:48 PM
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        out = []
        for i in range(len(prices)):
            out.append(prices[i])
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    out[i]=prices[i]-prices[j]
                    break
            
        return out
                
            
            
            
        