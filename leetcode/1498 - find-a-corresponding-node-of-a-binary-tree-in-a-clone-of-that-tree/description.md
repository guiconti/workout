Given two binary trees `` original `` and `` cloned `` and given a reference to a node `` target `` in the original tree.

The `` cloned `` tree is a __copy of__ the `` original `` tree.

Return _a reference to the same node_ in the `` cloned `` tree.

__Note__ that you are __not allowed__ to change any of the two trees or the `` target `` node and the answer __must be__ a reference to a node in the `` cloned `` tree.

__Follow up:__&nbsp;Solve the problem if repeated values on the tree are allowed.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/21/e1.png" style="width: 544px; height: 426px;"/>

<pre>
<strong>Input:</strong> tree = [7,4,3,null,null,6,19], target = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/21/e2.png" style="width: 221px; height: 159px;"/>

<pre>
<strong>Input:</strong> tree = [7], target =  7
<strong>Output:</strong> 7
</pre>

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/21/e3.png" style="width: 459px; height: 486px;"/>

<pre>
<strong>Input:</strong> tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
<strong>Output:</strong> 4
</pre>

__Example 4:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/21/e4.png" style="width: 555px; height: 239px;"/>

<pre>
<strong>Input:</strong> tree = [1,2,3,4,5,6,7,8,9,10], target = 5
<strong>Output:</strong> 5
</pre>

__Example 5:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/21/e5.png" style="width: 427px; height: 345px;"/>

<pre>
<strong>Input:</strong> tree = [1,2,null,3], target = 2
<strong>Output:</strong> 2
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the `` tree `` is in the range `` [1, 10^4] ``.
*   The values of the nodes of the `` tree `` are unique.
*   `` target `` node is a&nbsp;node from the `` original `` tree and is not `` null ``.