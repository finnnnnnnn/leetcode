#!python3

class MinStack:
    def __init__(self):
        self.s=[]
        
    def push(self,x):
        self.s.append(x)
    
    def pop(self):
        self.s.pop()

    def top(self):
        if len(self.s)==0:
            return None
        else:
            return self.s[-1]
    def getMin(self):
        if len(self.s)==0:
            return None
        else:
            return min(self.s)
if __name__=='__main__':
    s=MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    print(s.getMin())
    s.pop()
    print(s.top())
    print(s.getMin())
