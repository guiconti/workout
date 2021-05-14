You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
<strong>Output:</strong> [1,2,3,7,8,11,12,9,10,4,5,6]
<strong>Explanation:
</strong>
The multilevel linked list in the input is as follows:

<img src="https://assets.leetcode.com/uploads/2018/10/12/multilevellinkedlist.png" style="width: 640px;"/>

After flattening the multilevel linked list it becomes:

<img src="https://assets.leetcode.com/uploads/2018/10/12/multilevellinkedlistflattened.png" style="width: 1100px;"/>
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> head = [1,2,null,3]
<strong>Output:</strong> [1,3,2]
<strong>Explanation:

</strong>The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> head = []
<strong>Output:</strong> []
</pre>

&nbsp;

__How&nbsp;multilevel linked list is represented in test case:__

We use the&nbsp;multilevel linked list from __Example 1__ above:

<pre>
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL</pre>

The serialization of each level is as follows:

<pre>
[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
</pre>

To serialize all levels together we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:

<pre>
[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
</pre>

Merging the serialization of each level and removing trailing nulls we obtain:

<pre>
[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]</pre>

&nbsp;

__Constraints:__

*   The number of Nodes will not exceed `` 1000 ``.
*   <code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code>