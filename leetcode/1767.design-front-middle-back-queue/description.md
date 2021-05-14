Design a queue that supports `` push `` and `` pop `` operations in the front, middle, and back.

Implement the `` FrontMiddleBack `` class:

*   `` FrontMiddleBack() `` Initializes the queue.
*   `` void pushFront(int val) `` Adds `` val `` to the __front__ of the queue.
*   `` void pushMiddle(int val) `` Adds `` val `` to the __middle__ of the queue.
*   `` void pushBack(int val) `` Adds `` val `` to the __back__ of the queue.
*   `` int popFront() `` Removes the __front__ element of the queue and returns it. If the queue is empty, return `` -1 ``.
*   `` int popMiddle() `` Removes the __middle__ element of the queue and returns it. If the queue is empty, return `` -1 ``.
*   `` int popBack() `` Removes the __back__ element of the queue and returns it. If the queue is empty, return `` -1 ``.

__Notice__ that when there are __two__ middle position choices, the operation is performed on the __frontmost__ middle position choice. For example:

*   Pushing `` 6 `` into the middle of `` [1, 2, 3, 4, 5] `` results in <code>[1, 2, <u>6</u>, 3, 4, 5]</code>.
*   Popping the middle from <code>[1, 2, <u>3</u>, 4, 5, 6]</code> returns `` 3 `` and results in `` [1, 2, 4, 5, 6] ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong>
["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
[[], [1], [2], [3], [4], [], [], [], [], []]
<strong>Output:</strong>
[null, null, null, null, null, 1, 3, 4, 2, -1]

<strong>Explanation:</strong>
FrontMiddleBackQueue q = new FrontMiddleBackQueue();
q.pushFront(1);   // [<u>1</u>]
q.pushBack(2);    // [1, <u>2</u>]
q.pushMiddle(3);  // [1, <u>3</u>, 2]
q.pushMiddle(4);  // [1, <u>4</u>, 3, 2]
q.popFront();     // return 1 -&gt; [4, 3, 2]
q.popMiddle();    // return 3 -&gt; [4, 2]
q.popMiddle();    // return 4 -&gt; [2]
q.popBack();      // return 2 -&gt; []
q.popFront();     // return -1 -&gt; [] (The queue is empty)
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= val &lt;= 10<sup>9</sup></code>
*   At most&nbsp;`` 1000 ``&nbsp;calls will be made to&nbsp;`` pushFront ``,&nbsp;`` pushMiddle ``,&nbsp;`` pushBack ``, `` popFront ``, `` popMiddle ``, and `` popBack ``.