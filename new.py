class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # sum from left to right 

        a = l1
        b = l2

        sum,carry = 0,0
        dummy = ListNode(-1)
        cur = dummy
        
        while a or  b or carry:
            # if any thing exists
            p = a.val if a else 0
            q = b.val if b else 0

            sum = p + q+ carry

            # 10 --> carry 1 ==> sum / 10 == carry, 

            cur.next = ListNode(sum%10)
            print(cur)
            carry = sum // 10

            cur = cur.next 

            if a:
                a=a.next
            if b:
                b = b.next

        while carry > 0:
            cur = ListNode(carry)

        return dummy.next
