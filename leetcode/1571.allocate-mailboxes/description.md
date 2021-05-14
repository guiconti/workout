Given the array `` houses `` and an integer `` k ``. where `` houses[i] `` is the location of the ith house along a street, your task is to allocate `` k `` mailboxes in&nbsp;the street.

Return the __minimum__ total distance between each house and its nearest mailbox.

The answer is guaranteed to fit in a 32-bit signed integer.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/05/07/sample_11_1816.png" style="width: 454px; height: 154px;"/>

<pre>
<strong>Input:</strong> houses = [1,4,8,10,20], k = 3
<strong>Output:</strong> 5
<strong>Explanation: </strong>Allocate mailboxes in position 3, 9 and 20.
Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5 
</pre>

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/05/07/sample_2_1816.png" style="width: 433px; height: 154px;"/></strong>

<pre>
<strong>Input:</strong> houses = [2,3,5,12,18], k = 2
<strong>Output:</strong> 9
<strong>Explanation: </strong>Allocate mailboxes in position 3 and 14.
Minimum total distance from each houses to nearest mailboxes is |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> houses = [7,4,6,1], k = 1
<strong>Output:</strong> 8
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> houses = [3,6,14,10], k = 4
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` n == houses.length ``
*   `` 1 &lt;= n&nbsp;&lt;= 100 ``
*   `` 1 &lt;= houses[i] &lt;= 10^4 ``
*   `` 1 &lt;= k &lt;= n ``
*   Array `` houses `` contain unique integers.