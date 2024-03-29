Design an iterator that supports the `` peek `` operation on a list in addition to the `` hasNext `` and the `` next `` operations.

Implement the `` PeekingIterator `` class:

*   `` PeekingIterator(int[] nums) `` Initializes the object with the given integer array `` nums ``.
*   `` int next() `` Returns the next element in the array and moves the pointer to the next element.
*   `` bool hasNext() `` Returns `` true `` if there are still elements in the array.
*   `` int peek() `` Returns the next element in the array __without__ moving the pointer.

&nbsp;

__Example 1:__

<pre>
<strong>Input</strong>
["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
[[[1, 2, 3]], [], [], [], [], []]
<strong>Output</strong>
[null, 1, 2, 2, 3, false]

<strong>Explanation</strong>
PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [<u><strong>1</strong></u>,2,3]
peekingIterator.next();    // return 1, the pointer moves to the next element [1,<u><strong>2</strong></u>,3].
peekingIterator.peek();    // return 2, the pointer does not move [1,<u><strong>2</strong></u>,3].
peekingIterator.next();    // return 2, the pointer moves to the next element [1,2,<u><strong>3</strong></u>]
peekingIterator.next();    // return 3, the pointer moves to the next element [1,2,3]
peekingIterator.hasNext(); // return False
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 1000 ``
*   `` 1 &lt;= nums[i] &lt;= 1000 ``
*   All the calls to `` next `` and `` peek `` are valid.
*   At most `` 1000 `` calls will be made to `` next ``, `` hasNext ``, and `` peek ``.

&nbsp;
__Follow up:__ How would you extend your design to be generic and work with all types, not just integer?