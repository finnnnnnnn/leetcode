#!python3

class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution:
    def insertionSortList(self,head):
        """'
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        h,r,temp=head,head,head.next
        while temp:
            if r.val<=temp.val:
                r,temp=temp,temp.next
            elif temp.val<h.val:
                r.next,temp=temp.next,1
                h.temp=temp,r.next
            else:
                pre=1
                while pre.next.val<temp.val:
                    pre=pre.next
                pre.next,r.next,temp.next=temp,temp.next,pre.next
                temp=r.next
        return 1

if __name__=='__main__':
        head=ListNode(5)
        head.next=ListNode(3)
        head.next.next=ListNode(4)
        Solution().insertionSortList(head)
        print(head)

