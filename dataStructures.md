# Data structures

## Implementation

You can find the implementation for the 5 data structures in data_structures.py

You can run the code using:

```
python data_structures.py
```

## Time Complexity

### Array

In my Array implementation, the get, push and pop operations are all in constant time (O(1)), depending on the underlying list to do so.

The delete operation however requires shifting all the subsequent elements to the left, requiring a complexity of O(n).

### Matrix

All operations in the Matrix class: get, set and delete, have O(1) complexity, using the underlying hashmap dictionary to achieve this.

### Stack

All stack operations are achieved in O(1), since they directly depend on the get, push and pop operations from the Array

### Queue

For the Queue, the enqueue and peek operations are achieved in O(1), since they use the get and push operations from the Array.

However, the dequeue operation requires O(n) since it depends on the delete operation from the Array, and requires shifting all elements to the left. This is a case in which a Linked List would be more efficient.

### Linked List

In the linked list, only the append operation is in O(1), since we have direct access to the tail node.

The insert, delete and traverse operations require O(n) time, since they need to traverse the queue until they reach the specified index in order to modify the list.

## Arrays vs Linked lists for Stack and Queue

For my implementations, I went with Array implementations for my Stack and Queue classes.

The advantage of the Array implementation is that it provides a smaller memory footprint (of only O(n)), and provides easy random access to the array, useful for peek and pop functions.

The disadvantages come from arrays having a fixed size, which comes with a performance hit when the array needs to be resized; deleting elements at random positions also requires shifting the array elements, which is an O(n) operation on an array.

Linked Lists on the other hand have a dynamic size by nature, thus not suffering the performance hit. Inserting or removing elements at the beginning and end of a linked list is also very efficient, which makes them suitable for queues.

However, they also come with a larger memory footprint, since each element needs to store a pointer to the next node in the list. In small datasets, this can be a significant increase in memory usage.

## Efficiency of data structures in specific scenarios

### Random Access

For random access, the Array and Matrix classes are the fastest, being able to access their elements in O(1), as detailed above. This also leads to my Stack and Queue implementations also achieving O(1) time, since they are based on the Array class.

The Linked list is most inefficient for random access, requiring sequential accessing of the elements.

### Insertion and deletion

The Array implemetantion is inefficient for insertion and deletion at atrbitrary positions, however it can insert or delete elements at the end in O(1).

The matrix achieves O(1) on all operations, since it uses an underlying dictionary to store the data.

The linked list is the most efficient for inserting at random positions, as detailed above.

The stack and queue implementations are efficient for insertions on one end and deletitions on the other, but they are inefficient at random positions.

### Searching for a specific element

The array and matrix achieve linear time for searching for a specific element, and they are suitable for binary search if sorted.

The linked list is inefficient for searching, since elements have to be be accessed sequentially.

The stack and queue are not meant to be used in search scenarios, so they are inefficient: all elements have to be checked individually in order to find the desired element.

## Discussion

There are numerous practical applications for these data structures, and cases in which one may be preferred over the other.

Arrays are a basic data structure; they are used for various numerical computations requiring a list of items, but also for complex tasks like image processing; they are uniquely suited for representing a list of pixels and performing manipulations on it.

Matrixes are used in data analysis, their mathematical properties being very well-studied and providing quick ways to manipulate their contents and derive information from them. They are also vital for linear algebra and in the field of computer graphics, which are based on matrix transformations.

Queues are often used for task scheduling, being able to quickly pull out the next task, as well as add a new one. They are also used by operating system to specify the order in which processes should run.

Stacks are famously used for the function stack used by almost all programming languages: they are also useful for certain algorithms such as backtracking ones, and for storing a list of the actions a user is doing in order to provide undo / redo functionality.

Linked lists can be used to store graphs, allowing for an arbitrary increase in the number of nodes at any time without requiring shifting the underlying data.

As seen above, there are scenarios where each data structure is the most optimal to use. For example, if memory usage is a concern, an array would be used as opposed to a linked list. However, if memory is available and the user needs to manage a dynamic list of tasks, a linked list would be a better option since the sequence of the elements can change as needed.

A linked list would also be the obvious option to implement something like a search engine, due to the ease in which graphs can be implemented and traversed using it.
