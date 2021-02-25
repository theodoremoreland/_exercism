class Element:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, list_of_elements=[]):
        self.head = None
        self.length = 0

        for element in list_of_elements:
            if isinstance(element, Element):
                self.add(element)
            else:
                element = Element(element)
                self.add(element)

    def add(self, element):
        if self.head == None:
            self.head = element
        else:
            element.next = self.head
            self.head = element
        self.length += 1

    def to_list(self):
        _list = []
        current_node = self.head

        if not current_node:
            return _list
        else:
            _list.append(current_node.value)
            while current_node.next:
                current_node = current_node.next
                _list.append(current_node.value)
            return _list
    
    def reverse(self):
        if not self.head:
            return self
        else:
            new_head = self.head
            self.head = None

            while new_head:
                ephemeral_head = new_head.next
                new_head.next = None
                self.add(new_head)
                new_head = ephemeral_head

            return self