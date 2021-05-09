Implement the `` BSTIterator `` class that represents an iterator over the __<a href="https://en.wikipedia.org/wiki/Tree_traversal#In-order_(LNR)" target="_blank">in-order traversal</a>__ of a binary search tree (BST):

*   `` BSTIterator(TreeNode root) `` Initializes an object of the `` BSTIterator `` class. The `` root `` of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
*   `` boolean hasNext() `` Returns `` true `` if there exists a number in the traversal to the right of the pointer, otherwise returns `` false ``.
*   `` int next() `` Moves the pointer to the right, then returns the number at the pointer.

Notice that by initializing the pointer to a non-existent smallest number, the first call to `` next() `` will return the smallest element in the BST.

You may assume that `` next() `` calls will always be valid. That is, there will be at least a next number in the in-order traversal when `` next() `` is called.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/25/bst-tree.png" style="width: 189px; height: 178px;"/>

<pre>
<strong>Input</strong>
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
<strong>Output</strong>
[null, 3, 7, true, 9, true, 15, true, 20, false]

<strong>Explanation</strong>
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range <code>[1, 10<sup>5</sup>]</code>.
*   <code>0 &lt;= Node.val &lt;= 10<sup>6</sup></code>
*   At most <code>10<sup>5</sup></code> calls will be made to `` hasNext ``, and `` next ``.

&nbsp;

__Follow up:__

*   Could you implement `` next() `` and `` hasNext() `` to run in average `` O(1) `` time and use&nbsp;`` O(h) `` memory, where `` h `` is the height of the tree?