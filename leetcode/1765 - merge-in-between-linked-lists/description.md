You are given two linked lists: `` list1 `` and `` list2 `` of sizes `` n `` and `` m `` respectively.

Remove `` list1 ``'s nodes from the <code>a<sup>th</sup></code> node to the <code>b<sup>th</sup></code> node, and put `` list2 `` in their place.

The blue edges and nodes in the following figure incidate the result:

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/fig1.png" style="height: 130px; width: 504px;"/>

_Build the result list and return its head._

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/merge_linked_list_ex1.png" style="width: 406px; height: 140px;"/>

<pre>
<strong>Input:</strong> list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
<strong>Output:</strong> [0,1,2,1000000,1000001,1000002,5]
<strong>Explanation:</strong> We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/merge_linked_list_ex2.png" style="width: 463px; height: 140px;"/>

<pre>
<strong>Input:</strong> list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
<strong>Output:</strong> [0,1,1000000,1000001,1000002,1000003,1000004,6]
<strong>Explanation:</strong> The blue edges and nodes in the above figure indicate the result.
</pre>

&nbsp;

__Constraints:__

*   <code>3 &lt;= list1.length &lt;= 10<sup>4</sup></code>
*   `` 1 &lt;= a &lt;= b &lt; list1.length - 1 ``
*   <code>1 &lt;= list2.length &lt;= 10<sup>4</sup></code>