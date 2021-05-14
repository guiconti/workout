Given the heads of two singly linked-lists `` headA `` and `` headB ``, return _the node at which the two lists intersect_. If the two linked lists have no intersection at all, return `` null ``.

For example, the following two linked lists begin to intersect at node `` c1 ``:

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/05/160_statement.png" style="width: 500px; height: 162px;"/>

It is __guaranteed__ that there are no cycles anywhere in the entire linked structure.

__Note__ that the linked lists must __retain their original structure__ after the function returns.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/05/160_example_1_1.png" style="width: 742px; height: 241px;"/>

<pre>
<strong>Input:</strong> intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
<strong>Output:</strong> Intersected at '8'
<strong>Explanation:</strong> The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/05/160_example_2.png" style="width: 622px; height: 241px;"/>

<pre>
<strong>Input:</strong> intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
<strong>Output:</strong> Intersected at '2'
<strong>Explanation:</strong> The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
</pre>

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/05/160_example_3.png" style="width: 382px; height: 241px;"/>

<pre>
<strong>Input:</strong> intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
<strong>Output:</strong> No intersection
<strong>Explanation:</strong> From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
</pre>

&nbsp;

__Constraints:__

*   The number of nodes of `` listA `` is in the `` m ``.
*   The number of nodes of `` listB `` is in the `` n ``.
*   <code>0 &lt;= m, n &lt;= 3 * 10<sup>4</sup></code>
*   <code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code>
*   `` 0 &lt;= skipA &lt;= m ``
*   `` 0 &lt;= skipB &lt;= n ``
*   `` intersectVal `` is `` 0 `` if `` listA `` and `` listB `` do not intersect.
*   `` intersectVal == listA[skipA + 1] == listB[skipB + 1] `` if `` listA `` and `` listB `` intersect.

&nbsp;
__Follow up:__ Could you write a solution that runs in `` O(n) `` time and use only `` O(1) `` memory?