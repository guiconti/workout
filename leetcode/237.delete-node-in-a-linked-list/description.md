Write a function to __delete a node__ in a singly-linked list. You will __not__ be given access to the `` head `` of the list, instead you will be given access to __the node to be deleted__ directly.

It is __guaranteed__ that the node to be deleted is __not a tail node__ in the list.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/01/node1.jpg" style="width: 450px; height: 322px;"/>

<pre>
<strong>Input:</strong> head = [4,5,1,9], node = 5
<strong>Output:</strong> [4,1,9]
<strong>Explanation: </strong>You are given the second node with value 5, the linked list should become 4 -&gt; 1 -&gt; 9 after calling your function.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/01/node2.jpg" style="width: 450px; height: 354px;"/>

<pre>
<strong>Input:</strong> head = [4,5,1,9], node = 1
<strong>Output:</strong> [4,5,9]
<strong>Explanation: </strong>You are given the third node with value 1, the linked list should become 4 -&gt; 5 -&gt; 9 after calling your function.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> head = [1,2,3,4], node = 3
<strong>Output:</strong> [1,2,4]
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> head = [0,1], node = 0
<strong>Output:</strong> [1]
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> head = [-3,5,-99], node = -3
<strong>Output:</strong> [5,-99]
</pre>

&nbsp;

__Constraints:__

*   The number of the nodes in the given list is in the range `` [2, 1000] ``.
*   `` -1000 &lt;= Node.val &lt;= 1000 ``
*   The value of each node in the list is __unique__.
*   The `` node `` to be deleted is __in the list__ and is __not a tail__ node