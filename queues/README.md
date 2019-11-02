3 types of queue:
list_queue.py is the simplist, implementing the bultin list class using insert(0) to enqueue and pop() to dequeue.

stack_queue.py uses a pair of stacks (implemented in ../stack) to optimize for many subsequent enqueues or dequeues. Works by pushing enqueues onto an incoming stack, and when asked to dequeue it flips the stack into outgoing stack and pops from there.

node_queue.py is a pointer version of the queue. Implemented very similar to the doubly linked list but without search or deletion etc, and enqueue and dequeue instead.

Some uses are:
 * undo and redo buttons
 * back and forward webpage buttons
 * keeping track of function calls for recursion
 * the ide uses it to check for correct bracket/ parenthesis syntax
