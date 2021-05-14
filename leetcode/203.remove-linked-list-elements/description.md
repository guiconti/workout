Given the `` head `` of a linked list and an integer `` val ``, remove all the nodes of the linked list that has `` Node.val == val ``, and return _the new head_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg" style="width: 500px; height: 142px;"/>

<pre>
<strong>Input:</strong> head = [1,2,6,3,4,5,6], val = 6
<strong>Output:</strong> [1,2,3,4,5]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> head = [], val = 1
<strong>Output:</strong> []
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> head = [7,7,7,7], val = 7
<strong>Output:</strong> []
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the list is in the range <code>[0, 10<sup>4</sup>]</code>.
*   `` 1 &lt;= Node.val &lt;= 50 ``
*   `` 0 &lt;= k &lt;= 50 ``