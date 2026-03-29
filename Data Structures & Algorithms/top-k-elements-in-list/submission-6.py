class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # the frequency
        freq={}

        for num in nums:
           if num in freq:
            freq[num]+= 1

           else:
                freq[num] = 1

        # switch the number with it frequency
        bucket=[]

        for x in range(len(nums) +1):
            bucket.append([])

        for num in freq:
            count= freq[num]
            bucket[count].append(num)

        #find the more frequent number
        result= []

        for i in range(len(bucket) -1, -1, -1):
                for number in bucket[i]:
                    result.append(number)

                    if len(result) == k:
                        return result

        return result

        

