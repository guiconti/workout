Design your implementation of the linked list. You can choose to use a singly or doubly linked list.  
A node in a singly linked list should have two attributes: `` val `` and `` next ``. `` val `` is the value of the current node, and `` next `` is a pointer/reference to the next node.  
If you want to use the doubly linked list, you will need one more attribute `` prev `` to indicate the previous node in the linked list. Assume all nodes in the linked list are __0-indexed__.

Implement the `` MyLinkedList `` class:

*   `` MyLinkedList() `` Initializes the `` MyLinkedList `` object.
*   `` int get(int index) `` Get the value of the <code>index<sup>th</sup></code> node in the linked list. If the index is invalid, return `` -1 ``.
*   `` void addAtHead(int val) `` Add a node of value `` val `` before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
*   `` void addAtTail(int val) `` Append a node of value `` val `` as the last element of the linked list.
*   `` void addAtIndex(int index, int val) `` Add a node of value `` val `` before the <code>index<sup>th</sup></code> node in the linked list. If `` index `` equals the length of the linked list, the node will be appended to the end of the linked list. If `` index `` is greater than the length, the node __will not be inserted__.
*   `` void deleteAtIndex(int index) `` Delete the <code>index<sup>th</sup></code> node in the linked list, if the index is valid.

&nbsp;

__Example 1:__

<pre>
<strong>Input</strong>
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
<strong>Output</strong>
[null, null, null, null, 2, null, 3]

<strong>Explanation</strong>
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1-&gt;2-&gt;3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1-&gt;3
myLinkedList.get(1);              // return 3
</pre>

&nbsp;

__Constraints:__

*   `` 0 &lt;= index, val &lt;= 1000 ``
*   Please do not use the built-in LinkedList library.
*   At most `` 2000 `` calls will be made to `` get ``, `` addAtHead ``, `` addAtTail ``, `` addAtIndex `` and `` deleteAtIndex ``.