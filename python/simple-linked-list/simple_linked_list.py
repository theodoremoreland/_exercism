# export class Element {
#   constructor(value) {
#     this._value = value;
#     this._next = null;
#   }

#   get value() {
#     return this._value;
#   }

#   set value(value) {
#     this._value = value;
#   }

#   get next() {
#     return this._next;
#   }

#   set next(nextElement) {
#     this._next = nextElement;
#   }
# };


# export class List {
#   constructor(arrayOfElements) {
#     this._head = null;

#     if (Array.isArray(arrayOfElements)) {
#       arrayOfElements.forEach((element) => {
#         if (element instanceof Element) {
#           this.add(element)
#         }
#         else {
#           element = new Element(element);
#           this.add(element);
#         }
#       });
#     };
#   }


#   get head() {
#     return this._head;
#   }


#   get tail() {
#     let currentNode = this._head;
#     let tail;

#     while (currentNode.next) {
#       currentNode = currentNode.next;
#     };

#     tail = currentNode;
#     return tail;
#   }


#   nthNode(nth) {
#     let currentNode = this._head;
#     let nthNode = currentNode;

#     // Starts with 1 already counted (i.g. this._head)
#     for (let i = 1; i < nth; i++) {
#       nthNode = nthNode.next;
#       if (!nthNode) { break; }
#     };

#     return nthNode;
#   }


#   get length() {
#     let numberOfNodes;
#     let currentNode = this._head;

#     if (currentNode === null) {
#       numberOfNodes = 0;
#     }
#     else {
#       numberOfNodes = 1;

#       while (currentNode.next) {
#         numberOfNodes++;
#         currentNode = currentNode.next;
#       };
#     }

#     return numberOfNodes;
#   }


#   add(element) {
#     if (this._head === null) {
#       this._head = element;
#     }
#     else {
#       element.next = this._head;
#       this._head = element;
#     }
#   }


#   toArray() {
#     const array = [];
#     let currentNode = this._head;

#     if (!currentNode) {
#       return array;
#     }
#     else {
#       do {
#         array.push(currentNode.value);
#         currentNode = currentNode.next;
#       } while (currentNode);

#       return array;
#     };
#   }


#   reverse() {
#     if (!this._head) { return this; }

#     let newHead = this._head;
#     this._head = null; // Detaches head / resets current LinkedList

#     do {
#       let ephemeralHead = newHead.next;
#       newHead.next = null; // Detaches new head from ephemeral LinkedList
#       this.add(newHead); // Adds new head back to LinkedList
#       newHead = ephemeralHead; // Assigns potential new head
#     } while(newHead);

#     return this;
#   }
# };


# class Element:
#     def __init__(self, value):
#         pass

# class LinkedList:
#     def __init__(self):
#         pass


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
