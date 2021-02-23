export class Element {
  constructor(value) {
    this._value = value;
    this._next = null;
  }

  get value() {
    return this._value;
  }

  set value(value) {
    this._value = value;
  }

  get next() {
    return this._next;
  }

  set next(nextElement) {
    this._next = nextElement;
  }
};


export class List {
  constructor(arrayOfElements) {
    this._head = null;

    if (Array.isArray(arrayOfElements)) {
      arrayOfElements.forEach((element) => {
        if (element instanceof Element) {
          this.add(element)
        }
        else {
          element = new Element(element);
          this.add(element);
        }
      });
    };
  }


  get head() {
    return this._head;
  }


  get tail() {
    let currentNode = this._head;
    let tail;

    while (currentNode.next) {
      currentNode = currentNode.next;
    };

    tail = currentNode;
    return tail;
  }


  nthNode(nth) {
    let currentNode = this._head;
    let nthNode = currentNode;

    // Starts with 1 already counted (i.g. this._head)
    for (let i = 1; i < nth; i++) {
      nthNode = nthNode.next;
      if (!nthNode) { break; }
    };

    return nthNode;
  }


  get length() {
    let numberOfNodes;
    let currentNode = this._head;

    if (currentNode === null) {
      numberOfNodes = 0;
    }
    else {
      numberOfNodes = 1;

      while (currentNode.next) {
        numberOfNodes++;
        currentNode = currentNode.next;
      };
    }

    return numberOfNodes;
  }


  add(element) {
    if (this._head === null) {
      this._head = element;
    }
    else {
      element.next = this._head;
      this._head = element;
    }
  }


  toArray() {
    const array = [];
    let currentNode = this._head;

    if (!currentNode) {
      return array;
    }
    else {
      do {
        array.push(currentNode.value);
        currentNode = currentNode.next;
      } while (currentNode);

      return array;
    };
  }


  reverse() {
    if (!this._head) { return this; }

    let newHead = this._head;
    this._head = null; // Detaches head / resets current LinkedList

    do {
      let ephemeralHead = newHead.next;
      newHead.next = null; // Detaches new head from ephemeral LinkedList
      this.add(newHead); // Adds new head back to LinkedList
      newHead = ephemeralHead; // Assigns potential new head
    } while(newHead);

    return this;
  }
};