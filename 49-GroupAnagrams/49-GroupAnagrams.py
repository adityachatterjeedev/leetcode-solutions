# Last updated: 6/16/2025, 3:22:59 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            sortedword = ''.join(sorted(word))
            hashmap[sortedword].append(word)
        
        return list(hashmap.values())