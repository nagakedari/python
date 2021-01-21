
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def add(self, new_item):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_item
        else:
            self.head = new_item

    def insertAfter(self, element_after, new_item):
        current = self.head
        if self.head:
            while current.next and current.value != element_after.value:
                current = current.next
            if current.value == element_after.value:
                next_element = current.next
                current.next = new_item
                new_item.next = next_element
            else:
                print('List doesn\'t have the element to add after')
        else:
            self.head = new_item
    
    def print_linked_list(self):
        current = self.head
        chain = ''
        if self.head:
            while current.next:
                chain+= str(current.value)+'-->'
                current = current.next
            chain+= str(current.value)
        print(chain)
    
    def remove(self, item):
        current = self.head
        prev = current
        if self.head:
            if current.value == item.value:
                self.head = current.next
            while current.next and current.value != item.value:
                prev = current
                current = current.next
            if current.value == item.value:
                prev.next = current.next
            else:
                print('list doesn\'t have the element {} to remove:'.format(item.head))

    def get_poisition(self, poisition):
        current = self.head
        if self.head:
            curr_poisition = 1
            while current.next and curr_poisition < poisition:
                current = current.next
                curr_poisition+= 1
            if curr_poisition == poisition:
                return current
            else:
                return None
        else:
            return None
    def insertAtPosition(self, new_item, position):
        current = self.head
        if self.head:
            if position == 1:
                new_item.next = current
                self.head = new_item
            else:
                curr_position = 1
                prev = current
                while current.next and curr_position < position:
                    prev = current
                    current = current.next
                    curr_position+= 1
                if curr_position == position:
                    prev.next = new_item
                    new_item.next = current
                else:
                    print('List doesn\'t have the position')
        else:
            self.head = new_item


element1 = Element(10)
linked_list = LinkedList(element1)
element2 = Element(20)
element3 = Element(40)
linked_list.add(element2)
linked_list.add(element3)
element4 = Element(30)
linked_list.print_linked_list()
linked_list.insertAfter(element2,element4)
linked_list.print_linked_list()
linked_list.insertAfter(Element(30),Element(35))
linked_list.print_linked_list()
linked_list.add(Element(35))
linked_list.print_linked_list()
linked_list.remove(Element(35))
linked_list.print_linked_list()
position_value = linked_list.get_poisition(6).value if linked_list.get_poisition(6) else None
print(position_value)
linked_list.insertAtPosition(Element(45),1)
linked_list.print_linked_list()

linked_list.remove(Element(45))
linked_list.print_linked_list()
    