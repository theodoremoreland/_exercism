import unittest

from simple_linked_list import LinkedList, Element


class ElementClassTest(unittest.TestCase):
    def test_Element_has_constructor(self):
        element = Element(1)
        self.assertEqual(element.value, 1)

    def test_value_has_constructor_arg(self):
        element = Element(2)
        self.assertEqual(element.value, 2)

    def test_has_None_for_next_by_default(self):
        element = Element(2)
        self.assertIsNone(element.next)


class SimpleLinkedListClassTest(unittest.TestCase):
    def test_LinkedList_has_constructor(self):
        linked_list = LinkedList()
        self.assertIsInstance(linked_list, LinkedList)

    def test_new_LinkedList_should_have_length_0(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.length, 0)

    def test_can_add_element_to_LinkedList(self):
        linked_list = LinkedList()
        element = Element(4)
        try:
            linked_list.add(element)
        except Exception as e:
            self.fail(f"{e}")

    def test_adding_element_to_LinkedList_increments_length(self):
        linked_list = LinkedList()
        element = Element(4)
        linked_list.add(element)
        self.assertEqual(linked_list.length, 1)

    def test_adding_two_elements_to_LinkedList_increments_length_twice(self):
        linked_list = LinkedList()
        element_1 = Element(4)
        element_2 = Element(3)
        linked_list.add(element_1)
        linked_list.add(element_2)
        self.assertEqual(linked_list.length, 2)

    def test_new_LinkedList_have_a_None_head_element(self):
        linked_list = LinkedList()
        self.assertIsNone(linked_list.head)

    def test_adding_element_to_empty_LinkedList_sets_head(self):
        linked_list = LinkedList()
        element = Element(1)
        linked_list.add(element)
        self.assertIsInstance(linked_list.head, Element)

    def test_adding_a_second_element_updates_the_head(self):
        linked_list = LinkedList()
        element_1 = Element(1)
        element_2 = Element(3)
        linked_list.add(element_1)
        linked_list.add(element_2)
        self.assertEqual(linked_list.head.value, 3)


    def test_can_get_the_next_element_from_head(self):
        linked_list = LinkedList()
        element_1 = Element(1)
        element_2 = Element(3)
        linked_list.add(element_1)
        linked_list.add(element_2)
        self.assertEqual(linked_list.head.next.value, 1)

    def test_LinkedList_can_be_initialized_with_a_list(self):
        linked_list = LinkedList([1,2,3])
        self.assertEqual(linked_list.length, 3)
        self.assertEqual(linked_list.head.value, 3)


class SimpleLinkedListWithMultipleElementsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.linked_list = LinkedList([1,2,3,4,5,6,7,8,9,10])

    @classmethod
    def tearDownClass(cls):
        pass

    def test_has_correct_length(self):
        self.assertEqual(self.linked_list.length, 10)

    def test_has_correct_head_value(self):
        self.assertEqual(self.linked_list.head.value, 10)

    def test_can_traverse_LinkedList(self):
        self.assertEqual(self.linked_list.head.next.next.next.value, 7)

    def test_can_convert_to_list(self):
        linked_list = LinkedList([1])
        self.assertListEqual(linked_list.to_list(), [1])

    def test_head_of_LinkedList_is_final_element_from_input_list(self):
        linked_list = LinkedList([1, 2])
        self.assertEqual(linked_list.head.value, 2)

    def test_can_convert_longer_linkedList_to_list(self):
        self.assertListEqual(self.linked_list.to_list(), [10,9,8,7,6,5,4,3,2,1])

    def test_can_be_reversed(self):
        linked_list = LinkedList([1, 2])
        self.assertListEqual(linked_list.reverse().to_list(), [1,2])

    def test_can_be_reversed_when_it_has_more_elements(self):
        linked_list = LinkedList([1, 2, 3])
        self.assertListEqual(linked_list.reverse().to_list(), [1,2,3])

    def test_can_be_reversed_with_many_elements(self):
        linked_list = LinkedList([1,2,3,4,5,6,7,8,9,10])
        self.assertListEqual(linked_list.reverse().to_list(), [1,2,3,4,5,6,7,8,9,10])

    def test_can_reverse_a_reversal(self):
        linked_list = LinkedList([1,2,3,4,5,6,7,8,9,10])
        self.assertListEqual(linked_list.reverse().reverse().to_list(), [10,9,8,7,6,5,4,3,2,1])