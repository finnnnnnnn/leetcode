#!python3
class Solution:
    def asteroidCollision(self,asteroids):
        """
        :type asteroids:List[int]
        :rtype:List[int]
        """
        finalAster=[]
        direction=[]
        l,sign=len(asteroids),0
        for i in range(l):
            if len(finalAster)!=0:
                sign=asteroids[i]/abs(asteroids[i])
                if sign>=direction[-1] :
                    direction.append(sign)
                    finalAster.append(asteroids[i])
                else:
                    while sign<direction[-1]:
                        if finalAster[-1]>abs(asteroids[i]):
                            break
                        elif finalAster[-1]<abs(asteroids[i]): 
                            direction.pop()
                            finalAster.pop()
                            if len(finalAster)==0:
                                finalAster.append(asteroids[i])
                                direction.append(sign)
                        else:
                            direction.pop()
                            finalAster.pop()
                            break
            else:
                if asteroids[i]!=0:
                    direction.append(asteroids[i]/abs(asteroids[i]))
                    finalAster.append(asteroids[i])
                else:
                    print('No zero!')
        return finalAster

if __name__=='__main__':
    aster=[8,-8,10,2,-5]
    print(Solution().asteroidCollision(aster))
