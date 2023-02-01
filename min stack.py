class MinStack(object):

    def __init__(self):
        self.min = []
        
        self.minStack = []  

    def push(self, val):      
        if len(self.minStack) > 0 and  self.min[-1] >= val :          
            self.min.append(val) 

        if len(self.minStack) == 0:
            self.min.append(val)
        return self.minStack.append(val)
        
    def pop(self):
        if self.minStack[-1] == self.min[-1] :
            self.min.pop()
        return self.minStack.pop()
        
    def top(self):
        return self.minStack[-1]
        """
        :rtype: int
        """
        

    def getMin(self):
        return self.min[-1]
        """
        :rtype: int
        """
       
