Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

**These can all be constant time if doubly linked lists are implemented. 

1. What is the runtime complexity of `enqueue`?
  O(n) Linear Time -- Since we're using the .insert() method which has to account for updating all indicies of the list.
2. What is the runtime complexity of `dequeue`?
  O(n) Linear Time -- Dequeue is using the .pop() method which has to account for updating all indicies of the list
3. What is the runtime complexity of `len`? 
  O(1) Constant Time -- Since it is just reading the size propery, it is constant time.

## Binary Search Tree

1. What is the runtime complexity of `insert`? 
  O(n) Linear Time
2. What is the runtime complexity of `contains`?
  O(n) Linear Time
3. What is the runtime complexity of `get_max`? 
  I think O(logn)
## Heap

1. What is the runtime complexity of `_bubble_up`?
  O(logn)
2. What is the runtime complexity of `_sift_down`?
  O(logn)
3. What is the runtime complexity of `insert`?
  O(logn)
4. What is the runtime complexity of `delete`?
  O(logn)
5. What is the runtime complexity of `get_max`?
  O(1) Constant Time
## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
  O(1) Constant Time
2. What is the runtime complexity of `ListNode.insert_before`?
  O(1) Constant Time
3. What is the runtime complexity of `ListNode.delete`?
  O(1) Constant Time
4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
  O(1) Constant Time
5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
  O(1) Constant Time
6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
  O(1) Constant Time
7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
  O(1) Constant Time
8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
  O(1) Constant Time
9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
  O(1) Constant Time
10. What is the runtime complexity of `DoublyLinkedList.delete`?
  O(1) Constant Time
    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
      Array.splice takes Linear time since it has to iterate through the array to reassign indicies. 