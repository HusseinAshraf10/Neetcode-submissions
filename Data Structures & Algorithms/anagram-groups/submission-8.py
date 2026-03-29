class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap={}

        for word in strs:
            count= [0] * 26

            for char in word:
                index= ord(char) - ord("a")
                count[index]+= 1

            key= tuple(count)

            if key not in hashmap:
                hashmap[key]= []

            hashmap[key].append(word)

        return list(hashmap.values())

        
