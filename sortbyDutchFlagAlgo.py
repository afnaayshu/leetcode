class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def swap(self,arr,i1,i2):
        temp = arr[i1]
        arr[i1] = arr[i2]
        arr[i2] = temp
        
        
    def sort012(self, arr):
        # code here
      #using Dutch Flag algorithm for partitioning 3 items
        low =0;
        mid =0;
        high = len(arr) - 1;
        while(mid <= high):
            if arr[mid] == 0:
                self.swap(arr,mid,low)
                mid = mid+1
                low = low+1
            elif arr[mid] == 1:
                mid = mid +1 
            else :
                self.swap(arr,mid,high)
                high =  high - 1
