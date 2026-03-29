class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #Input: strs = ["act","pots","tops","cat","stop","hat"]
        #Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

        hashmap= {}

        for word in strs:
            key= "".join(sorted(word))

            if key not in hashmap:
                hashmap[key] = []

            hashmap[key].append(word)

        return list(hashmap.values())
