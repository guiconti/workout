A conveyor belt has packages that must be shipped from one port to another within `` D `` days.

The <code>i<sup>th</sup></code> package on the conveyor belt has a weight of `` weights[i] ``. Each day, we load the ship with packages on the conveyor belt (in the order given by `` weights ``). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within `` D `` days.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> weights = [1,2,3,4,5,6,7,8,9,10], D = 5
<strong>Output:</strong> 15
<strong>Explanation:</strong> A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> weights = [3,2,2,4,1,4], D = 3
<strong>Output:</strong> 6
<strong>Explanation:</strong> A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> weights = [1,2,3,1,1], D = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong>
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= D &lt;= weights.length &lt;= 5 * 10<sup>4</sup></code>
*   `` 1 &lt;= weights[i] &lt;= 500 ``