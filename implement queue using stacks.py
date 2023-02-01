class MyQueue(object):

    def __init__(self):
        self.MyQueue =[]

    def push(self, x):
      return  self.MyQueue.append(x)
        

    def pop(self):
        return self.MyQueue.pop(0)
        """
        :rtype: int
        """
        

    def peek(self):
        return self.MyQueue[0]
        """
        :rtype: int
        """
        

    def empty(self):
        return len(self.MyQueue) == 0
        """
        :rtype: bool
        """
       
Console
