#!python3

class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution:
    def addTwoNumbers(self,l1,l2):
        """
        :type l1:ListNode
        :type l2:ListNode
        :rtype:ListNode
        """
        head=ListNode(0)
        p=head
        t=0
        h=0
        while l1 or l2:
            if l1:
                t+=l1.val
                l1=l1.next
            if l2:
                t+=l2.val
                l2=l2.next
            t,r=divmod(t,10)
            p.next=ListNode(r)
            p=p.next
        return head.next

if __name__=="__main__":
    l1=ListNode(2)
    l1.next=ListNode(4)
    l1.next.next=ListNode(3)
    l2=ListNode(5)
    l2.next=ListNode(6)
    l2.next.next=ListNode(4)
    l=Solution().addTwoNumbers(l1,l2)
    print("2->4->3 + 5->6->4 =",l.val,"->",l.next.val,"->",l.next.next.val)




            

