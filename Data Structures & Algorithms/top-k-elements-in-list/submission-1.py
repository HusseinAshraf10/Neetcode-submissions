class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq={}

        for num in nums:
            if num in freq:
                freq[num]+= 1
            else:
                freq[num]=1

        bucket=[]

        for x in range(len(nums)+1):
            bucket.append([])

        for num in freq:
                count= freq[num]
                bucket[count].append(num)

        result=[]

        for i in range(len(bucket)-1, -1, -1):
            if bucket[i] != []:

                for num in bucket[i]:
                    result.append(num)

                    if len(result) == k:
                        return result

        return result


        


        

