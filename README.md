# Data Structures in Python 
## Author: Ángela Gómez 

Implementation of classic data structures from scratch using Python.

**Note**: This was guided by Claude in order to correct syntax errors, along with the recall of certain topics and tips. 

## Structures
- [x] Linked List
- [x] Stack
- [x] Queue
- [x] HashMap
- [x] Binary Search Tree
- [ ] Graph 
- [ ] Heap / Priority Queue
- [ ] Trie 

## How to run
```bash
python3 structures/linked_list.py
python3 structures/stack.py
python3 structures/queue.py
python3 structures/hash_map.py
python3 structures/binary_search_tree.py 
```

---

## Explanations

### Linked List
A sequence of nodes where each node stores data and a pointer to the next node. Unlike arrays, elements are not stored in contiguous memory — they are scattered in memory and connected through pointers.

**When to use:** frequent insertions/deletions at the beginning or middle of a list.

### Stack
A linear structure that follows the **LIFO** principle (Last In First Out). Think of a pile of plates — you always add and remove from the top.

Core operations: `push` (add to top), `pop` (remove from top), `peek` (look at top without removing).

**When to use:** undo/redo functionality, call stack in programming languages, backtracking algorithms.

### Queue
A linear structure that follows the **FIFO** principle (First In First Out). Think of a line at a concert — the first one in is the first one out.

Core operations: `enqueue` (add to back), `dequeue` (remove from front), `peek` (look at front).

**When to use:** task scheduling, print queues, breadth-first search in graphs.

### HashMap
A key-value store that uses a **hash function** to convert keys into array indexes, allowing O(1) access to any element. Collisions (two keys mapping to the same index) are handled with **chaining** — each index holds a list of key-value pairs.

Core operations: `set` (store key-value), `get` (retrieve by key), `delete` (remove by key).

**When to use:** caching, fast lookups, counting frequencies, avoiding duplicates.

### Binary Search Tree (BST)
A hierarchical structure where each node has at most two children — called `left` and `right`. Follows the **BST rule**: values smaller than the parent go left, larger go right. This makes search very efficient as you eliminate half the tree at each step.

Core operations: `insert`, `search`, `delete` (3 cases: no children, one child, two children — handled with an inorder successor).

**Note**: The difference between this data structure and a plain binary tree is that this one follows a  left < parent < right rule as it keeps the data organized from smallest to largest.  

**When to use:** fast search/insert/delete, sorted data, implementing maps and sets.

### Graph

### Heap / Priority Queue

### Trie 

---

## Time Complexity

| Operation | Linked List | Stack | Queue | HashMap | Binary Tree | BST |
|---|---|---|---|---|---|---|
| **Insert** | O(1) head / O(n) tail | O(1) | O(1) | O(1) avg | O(n) | O(log n) avg / O(n) worst |
| **Search** | O(n) | O(n) | O(n) | O(1) avg | O(n) | O(log n) avg / O(n) worst |
| **Delete** | O(n) | O(1) | O(1) | O(1) avg | O(n) | O(log n) avg / O(n) worst |
| **Access by index** | O(n) | O(n) | O(n) | O(1) avg | O(n) | N/A |

> avg = average case. Binary Tree degrades to O(n) when unbalanced (e.g. inserting sorted data creates a straight line).