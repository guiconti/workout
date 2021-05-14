Given the `` head `` of a singly linked list and two integers `` left `` and `` right `` where `` left &lt;= right ``, reverse the nodes of the list from position `` left `` to position `` right ``, and return _the reversed list_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg" style="width: 542px; height: 222px;"/>

<pre>
<strong>Input:</strong> head = [1,2,3,4,5], left = 2, right = 4
<strong>Output:</strong> [1,4,3,2,5]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> head = [5], left = 1, right = 1
<strong>Output:</strong> [5]
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the list is `` n ``.
*   `` 1 &lt;= n &lt;= 500 ``
*   `` -500 &lt;= Node.val &lt;= 500 ``
*   `` 1 &lt;= left &lt;= right &lt;= n ``

&nbsp;
__Follow up:__ Could you do it in one pass?