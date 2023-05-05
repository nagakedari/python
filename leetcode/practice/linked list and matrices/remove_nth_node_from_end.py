class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_node_from_end(head, n):
    def find_list_length(head):
        count = 0
        while head:
            head = head.next
            count += 1
        return count

    def find_index_from_head(size, n):
        return size - n + 1

    if not head:
        return []

    curr_index = 1
    list_size = find_list_length(head)
    index_from_start = find_index_from_head(list_size, n)
    if list_size == n :
        head = head.next
        return head
    prev = temp = head
    while temp and curr_index < index_from_start:
        prev = temp
        temp = temp.next
        curr_index += 1
    prev.next = temp.next
    return head

def print_list(head):
    if head:
        nodes = [str(head.val)]
        traverser = head
        while traverser.next:
            traverser = traverser.next
            nodes.append(str(traverser.val))
    else:
        nodes = []

    print(f"Linked List: {'--->'.join(nodes)}")


def remove_nth_node_from_end_2_pointers(head, n):
    dummy_node = ListNode(-999, head)
    right = head
    left = dummy_node
    while n > 0 and right:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return dummy_node.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print_list(head)
    # print_list(remove_nth_node_from_end(head, 2))
    print_list(remove_nth_node_from_end_2_pointers(head, 2))

    head = ListNode(1)

    print_list(head)
    # print_list(remove_nth_node_from_end(head, 1))
    print_list(remove_nth_node_from_end_2_pointers(head, 2))

    head = ListNode(1)
    head.next = ListNode(2)

    print_list(head)
    # print_list(remove_nth_node_from_end(head, 1))
    print_list(remove_nth_node_from_end_2_pointers(head, 2))