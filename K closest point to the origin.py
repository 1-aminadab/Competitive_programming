class Solution(object):
    def kClosest(self, points, k):

        def calcDistance(index):
            point = points[index]
            distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
            return distance


        for i in range(len(points)):
            for j in range(len(points)-1):
                if calcDistance(j) > calcDistance(j + 1):
                    points[j], points[j+1] = points[j+1], points[j]

        return points[0:k]
