class Solution(object):

    def fizzBuzz(self, n):
        
        i = []
        string = ""
        x = 1
        while x < n+1:

            if x % 3 == 0 and x % 5 == 0:
                i.append("FizzBuzz")
            elif x % 3 == 0:
                i.append("Fizz")
            elif x % 5 == 0:
                i.append("Buzz")
            else:
                i.append(string + str(x))

            x += 1
        return i


