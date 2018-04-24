#!python3
class Points:
    def __init__(self,a=0,b=0):
        self.x=a
        self.y=b

class Solution:
    def maxPoints(self,points):
        """
        :type points:List[Point]
        :rtype:int
        """
        l=len(points)
        num=0
        for i in range(l):
            dic={'i':1}
            same=0
            for j in range(i+1,l):
                tx,ty=points[j].x,points[j].y
                if tx==points[i].x and ty==points[i].y:
                    same+=1
                    continue
                if tx==points[i].x:
                    slope='i'
                else:
                    slope=(points[i].y-ty)*1.0/(points[i].x-tx)
                if slope not in dic:
                    dic[slope]=1
                dic[slope]+=1
            num=max(num,max(dic.values())+same)
        return num

if __name__=='__main__':
    p1=Points(1,1)
    p2=Points(2,2)
    p3=Points(3,3)
    points=[Points(1,1),Points(3,2),Points(5,3),Points(4,1),Points(2,3),Points(1,4)]
    print(Solution().maxPoints(points))
