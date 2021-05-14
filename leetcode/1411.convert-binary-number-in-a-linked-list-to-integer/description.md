Given `` head `` which is a reference node to&nbsp;a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the _decimal value_ of the number in the linked list.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/12/05/graph-1.png" style="width: 426px; height: 108px;"/>

<pre>
<strong>Input:</strong> head = [1,0,1]
<strong>Output:</strong> 5
<strong>Explanation:</strong> (101) in base 2 = (5) in base 10
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> head = [0]
<strong>Output:</strong> 0
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> head = [1]
<strong>Output:</strong> 1
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
<strong>Output:</strong> 18880
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> head = [0,0]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   The Linked List is not empty.
*   Number of nodes&nbsp;will not exceed `` 30 ``.
*   Each node's value is either&nbsp;`` 0 `` or `` 1 ``.