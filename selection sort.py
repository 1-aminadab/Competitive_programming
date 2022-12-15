def select(self, arr, i):
        for i in range(len(arr)):
            return arr[i]
    
    def selectionSort(self, arr,n):
        for n in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
