class Solution(object):
    def sortSentence(self, s):
        unOrderedList = s.split(" ")
        s = s.split(" ")

        for i in range(len(unOrderedList)):
            correctIndex = unOrderedList[i][-1]
            s[int(correctIndex)-1] = unOrderedList[i].replace("{}".format(correctIndex), "")

        s = " ".join(s)
        
        return "{}".format(s)
