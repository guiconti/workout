You are given an integer array `` nums `` with no duplicates. A __maximum binary tree__ can be built recursively from `` nums `` using the following algorithm:

1.   Create a root node whose value is the maximum value in `` nums ``.
2.   Recursively build the left subtree on the __subarray prefix__ to the __left__ of the maximum value.
3.   Recursively build the right subtree on the __subarray suffix__ to the __right__ of the maximum value.

Return _the __maximum binary tree__ built from _`` nums ``.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/12/24/tree1.jpg" style="width: 302px; height: 421px;"/>

<pre>
<strong>Input:</strong> nums = [3,2,1,6,0,5]
<strong>Output:</strong> [6,3,5,null,2,0,null,null,1]
<strong>Explanation:</strong> The recursive calls are as follow:
- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
    - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
        - Empty array, so no child.
        - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
            - Empty array, so no child.
            - Only one element, so child is a node with value 1.
    - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
        - Only one element, so child is a node with value 0.
        - Empty array, so no child.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/12/24/tree2.jpg" style="width: 182px; height: 301px;"/>

<pre>
<strong>Input:</strong> nums = [3,2,1]
<strong>Output:</strong> [3,null,2,null,1]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 1000 ``
*   `` 0 &lt;= nums[i] &lt;= 1000 ``
*   All integers in `` nums `` are __unique__.