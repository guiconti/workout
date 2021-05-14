Design a stack which supports the following operations.

Implement the `` CustomStack `` class:

*   `` CustomStack(int maxSize) `` Initializes the object with `` maxSize `` which is the maximum number of elements in the stack or do nothing if the stack reached the `` maxSize ``.
*   `` void push(int x) ``&nbsp;Adds `` x `` to the top of the stack if the stack hasn't reached the `` maxSize ``.
*   `` int pop() ``&nbsp;Pops and returns the top of stack or __-1__ if the stack is empty.
*   `` void inc(int k, int val) `` Increments the bottom `` k `` elements of the stack by `` val ``. If there are less than `` k `` elements in the stack, just increment all the elements in the stack.

&nbsp;

__Example 1:__

<pre>
<strong>Input</strong>
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
<strong>Output</strong>
[null,null,null,2,null,null,null,null,null,103,202,201,-1]
<strong>Explanation</strong>
CustomStack customStack = new CustomStack(3); // Stack is Empty []
customStack.push(1);                          // stack becomes [1]
customStack.push(2);                          // stack becomes [1, 2]
customStack.pop();                            // return 2 --&gt; Return top of the stack 2, stack becomes [1]
customStack.push(2);                          // stack becomes [1, 2]
customStack.push(3);                          // stack becomes [1, 2, 3]
customStack.push(4);                          // stack still [1, 2, 3], Don't add another elements as size is 4
customStack.increment(5, 100);                // stack becomes [101, 102, 103]
customStack.increment(2, 100);                // stack becomes [201, 202, 103]
customStack.pop();                            // return 103 --&gt; Return top of the stack 103, stack becomes [201, 202]
customStack.pop();                            // return 202 --&gt; Return top of the stack 102, stack becomes [201]
customStack.pop();                            // return 201 --&gt; Return top of the stack 101, stack becomes []
customStack.pop();                            // return -1 --&gt; Stack is empty return -1.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= maxSize &lt;= 1000 ``
*   `` 1 &lt;= x &lt;= 1000 ``
*   `` 1 &lt;= k &lt;= 1000 ``
*   `` 0 &lt;= val &lt;= 100 ``
*   At most&nbsp;`` 1000 ``&nbsp;calls will be made to each method of `` increment ``, `` push `` and `` pop `` each separately.