Given a list of lists of integers,&nbsp;`` nums ``,&nbsp;return all elements of `` nums `` in diagonal order as shown in the below images.
&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/04/08/sample_1_1784.png" style="width: 158px; height: 143px;"/></strong>

<pre>
<strong>Input:</strong> nums = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [1,4,2,7,5,3,8,6,9]
</pre>

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/04/08/sample_2_1784.png" style="width: 230px; height: 177px;"/></strong>

<pre>
<strong>Input:</strong> nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
<strong>Output:</strong> [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
<strong>Output:</strong> [1,4,2,5,3,8,6,9,7,10,11]
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> nums = [[1,2,3,4,5,6]]
<strong>Output:</strong> [1,2,3,4,5,6]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 10^5 ``
*   `` 1 &lt;= nums[i].length &lt;=&nbsp;10^5 ``
*   `` 1 &lt;= nums[i][j] &lt;= 10^9 ``
*   There at most `` 10^5 `` elements in `` nums ``.