Given two sequences `` pushed `` and `` popped ``&nbsp;__with distinct values__,&nbsp;return `` true `` if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

&nbsp;

<div>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: </strong>pushed = <span id="example-input-1-1">[1,2,3,4,5]</span>, popped = <span id="example-input-1-2">[4,5,3,2,1]</span>
<strong>Output: </strong><span id="example-output-1">true</span>
<strong>Explanation: </strong>We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -&gt; 4,
push(5), pop() -&gt; 5, pop() -&gt; 3, pop() -&gt; 2, pop() -&gt; 1
</pre>
<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong>pushed = <span id="example-input-2-1">[1,2,3,4,5]</span>, popped = <span id="example-input-2-2">[4,3,5,1,2]</span>
<strong>Output: </strong><span id="example-output-2">false</span>
<strong>Explanation: </strong>1 cannot be popped before 2.
</pre>
</div>
</div>

&nbsp;

__Constraints:__

*   `` 0 &lt;= pushed.length == popped.length &lt;= 1000 ``
*   `` 0 &lt;= pushed[i], popped[i] &lt; 1000 ``
*   `` pushed `` is a permutation of `` popped ``.
*   `` pushed `` and `` popped `` have distinct values.