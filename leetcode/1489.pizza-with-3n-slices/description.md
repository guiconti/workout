There is a pizza with 3n slices of varying size, you and your friends will take slices of pizza as follows:

*   You will pick __any__ pizza slice.
*   Your friend Alice&nbsp;will pick&nbsp;next slice in anti clockwise direction of your pick.&nbsp;
*   Your friend Bob&nbsp;will&nbsp;pick&nbsp;next slice in clockwise direction of your pick.
*   Repeat&nbsp;until&nbsp;there are no more slices of pizzas.

Sizes of Pizza slices is represented by circular array `` slices `` in clockwise direction.

Return the maximum possible sum of slice sizes which you can have.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/18/sample_3_1723.png" style="width: 475px; height: 240px;"/>

<pre>
<strong>Input:</strong> slices = [1,2,3,4,5,6]
<strong>Output:</strong> 10
<strong>Explanation:</strong> Pick pizza slice of size 4, Alice and Bob will pick slices with size 3 and 5 respectively. Then Pick slices with size 6, finally Alice and Bob will pick slice of size 2 and 1 respectively. Total = 4 + 6.
</pre>

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/02/18/sample_4_1723.png" style="width: 475px; height: 250px;"/></strong>

<pre>
<strong>Input:</strong> slices = [8,9,8,6,1,1]
<strong>Output:</strong> 16
<strong>Output:</strong> Pick pizza slice of size 8 in each turn. If you pick slice with size 9 your partners will pick slices of size 8.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> slices = [4,1,2,5,8,3,1,9,7]
<strong>Output:</strong> 21
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> slices = [3,1,2]
<strong>Output:</strong> 3
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= slices.length &lt;= 500 ``
*   `` slices.length % 3 == 0 ``
*   `` 1 &lt;= slices[i] &lt;= 1000 ``