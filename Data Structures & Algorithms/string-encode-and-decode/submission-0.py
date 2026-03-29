class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string= ""

        for x in strs:
            length= len(x)
            length_str= str(length)
            encoded_word= length_str + "#" + x
            encoded_string+= encoded_word

        return encoded_string

    def decode(self, s: str) -> List[str]:

        result=[]
        x= 0
        while x < len(s):
            length_str=""

            while s[x] != "#":
                length_str+= s[x]
                x+=1

            length=int(length_str)

            start= x + 1
            end = start + length

            word= s[start:end]

            result.append(word)

            x= end

        return result



