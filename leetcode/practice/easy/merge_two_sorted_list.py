class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_lists(l1, l2):
    head = movingtail = ListNode()

    while l1 and l2:
        if l1.val <= l2.val:
            movingtail.next = l1
            l1 = l1.next
        else:
            movingtail.next = l2
            l2 = l2.next
        movingtail = movingtail.next
    movingtail.next = l1 or l2
    return head.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    merged_head = merge_lists(l1, l2)
    print(merged_head.val)
    print(merged_head.next.val)
    print(merged_head.next.next.val)
    print(merged_head.next.next.next.val)
    print(merged_head.next.next.next.next.val)
    # print(merged_head.next.val)
