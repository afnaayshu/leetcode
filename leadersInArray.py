class Solution:
    def leaders(self, arr):
        # code here
        length = len(arr)
        max = arr[length-1]
        leader = [max]
        i = length-2
        while(i>=0):
            if arr[i] >= max :
                max = arr[i]
                leader.append(max)
            i = i-1
        
        return leader.reverse()
