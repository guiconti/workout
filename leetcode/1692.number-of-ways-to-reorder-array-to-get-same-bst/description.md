Given an array `` nums ``&nbsp;that represents a permutation of integers from&nbsp;`` 1 ``&nbsp;to&nbsp;`` n ``. We are going to construct a binary search tree (BST) by inserting the elements of&nbsp;`` nums ``&nbsp;in&nbsp;order into an initially empty BST. Find the number of different ways to reorder `` nums `` so that the constructed BST is identical to that formed from the original array&nbsp;`` nums ``.

For example, given&nbsp;`` nums = [2,1,3] ``, we will have 2 as the root, 1 as a left child, and 3 as a right child. The array&nbsp;`` [2,3,1] ``&nbsp;also yields the same BST but&nbsp;`` [3,2,1] ``&nbsp;yields a different BST.

Return _the number of ways to reorder_&nbsp;`` nums ``&nbsp;_such that the BST formed is identical to the original BST formed from_&nbsp;`` nums ``.

Since the answer may be very large,&nbsp;__return it modulo&nbsp;__`` 10^9 + 7 ``.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/12/bb.png" style="width: 121px; height: 101px;"/>

<pre>
<strong>Input:</strong> nums = [2,1,3]
<strong>Output:</strong> 1
<strong>Explanation: </strong>We can reorder nums to be [2,3,1] which will yield the same BST. There are no other ways to reorder nums which will yield the same BST.
</pre>

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/08/12/ex1.png" style="width: 241px; height: 161px;"/></strong>

<pre>
<strong>Input:</strong> nums = [3,4,5,1,2]
<strong>Output:</strong> 5
<b>Explanation: </b>The following 5 arrays will yield the same BST: 
[3,1,2,4,5]
[3,1,4,2,5]
[3,1,4,5,2]
[3,4,1,2,5]
[3,4,1,5,2]
</pre>

__Example 3:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/08/12/ex4.png" style="width: 121px; height: 161px;"/></strong>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 0
<strong>Explanation: </strong>There are no other orderings of nums that will yield the same BST.
</pre>

__Example 4:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/08/12/abc.png" style="width: 241px; height: 161px;"/></strong>

<pre>
<strong>Input:</strong> nums = [3,1,2,5,4,6]
<strong>Output:</strong> 19
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> nums = [9,4,2,1,3,6,5,7,8,14,11,10,12,13,16,15,17,18]
<strong>Output:</strong> 216212978
<strong>Explanation: </strong>The number of ways to reorder nums to get the same BST is 3216212999. Taking this number modulo 10^9 + 7 gives 216212978.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 1000 ``
*   `` 1 &lt;= nums[i] &lt;= nums.length ``
*   All integers in&nbsp;`` nums ``&nbsp;are&nbsp;__distinct__.