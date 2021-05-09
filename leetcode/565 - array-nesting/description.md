You are given an integer array `` nums `` of length `` n `` where `` nums `` is a permutation of the numbers in the range `` [0, n - 1] ``.

You should build a set `` s[k] = {nums[k], nums[nums[i]], nums[nums[nums[k]]], ... } `` subjected to the following rule:

*   The first element in `` s[k] `` starts with the selection of the element `` nums[k] `` of `` index = k ``.
*   The next element in `` s[k] `` should be `` nums[nums[k]] ``, and then `` nums[nums[nums[k]]] ``, and so on.
*   We stop adding right before a duplicate element occurs in `` s[k] ``.

Return _the longest length of a set_ `` s[k] ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [5,4,0,3,1,6,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> 
nums[0] = 5, nums[1] = 4, nums[2] = 0, nums[3] = 3, nums[4] = 1, nums[5] = 6, nums[6] = 2.
One of the longest sets s[k]:
s[0] = {nums[0], nums[5], nums[6], nums[2]} = {5, 6, 2, 0}
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [0,1,2]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   `` 0 &lt;= nums[i] &lt; nums.length ``
*   All the values of `` nums `` are __unique__.