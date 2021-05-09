Given `` numBottles ``&nbsp;full water bottles, you can exchange `` numExchange `` empty water bottles for one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Return the __maximum__ number of water bottles you can&nbsp;drink.

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/07/01/sample_1_1875.png" style="width: 480px; height: 240px;"/></strong>

<pre>
<strong>Input:</strong> numBottles = 9, numExchange = 3
<strong>Output:</strong> 13
<strong>Explanation:</strong> You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can&nbsp;drink: 9 + 3 + 1 = 13.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/07/01/sample_2_1875.png" style="width: 790px; height: 290px;"/>

<pre>
<strong>Input:</strong> numBottles = 15, numExchange = 4
<strong>Output:</strong> 19
<strong>Explanation:</strong> You can exchange 4 empty bottles to get 1 full water bottle. 
Number of water bottles you can&nbsp;drink: 15 + 3 + 1 = 19.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> numBottles = 5, numExchange = 5
<strong>Output:</strong> 6
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> numBottles = 2, numExchange = 3
<strong>Output:</strong> 2
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;=&nbsp;numBottles &lt;= 100 ``
*   `` 2 &lt;=&nbsp;numExchange &lt;= 100 ``