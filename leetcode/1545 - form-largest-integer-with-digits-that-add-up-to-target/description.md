Given an array of integers `` cost `` and an integer `` target ``. Return the __maximum__ integer you can paint&nbsp;under the following rules:

*   The cost of painting a&nbsp;digit (i+1) is given by&nbsp;`` cost[i] ``&nbsp;(0 indexed).
*   The total cost used must&nbsp;be equal to `` target ``.
*   Integer does not have digits 0.

Since the answer may be too large, return it as string.

If there is no way to paint any integer given the condition, return "0".

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> cost = [4,3,2,5,6,7,2,5,5], target = 9
<strong>Output:</strong> "7772"
<strong>Explanation: </strong> The cost to paint the digit '7' is 2, and the digit '2' is 3. Then cost("7772") = 2*3+ 3*1 = 9. You could also paint "977", but "7772" is the largest number.
<strong>Digit    cost</strong>
  1  -&gt;   4
  2  -&gt;   3
  3  -&gt;   2
  4  -&gt;   5
  5  -&gt;   6
  6  -&gt;   7
  7  -&gt;   2
  8  -&gt;   5
  9  -&gt;   5
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> cost = [7,6,5,5,5,6,8,7,8], target = 12
<strong>Output:</strong> "85"
<strong>Explanation:</strong> The cost to paint the digit '8' is 7, and the digit '5' is 5. Then cost("85") = 7 + 5 = 12.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> cost = [2,4,6,2,4,6,4,4,4], target = 5
<strong>Output:</strong> "0"
<strong>Explanation:</strong> It's not possible to paint any integer with total cost equal to target.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> cost = [6,10,15,40,40,40,40,40,40], target = 47
<strong>Output:</strong> "32211"
</pre>

&nbsp;

__Constraints:__

*   `` cost.length == 9 ``
*   `` 1 &lt;= cost[i] &lt;= 5000 ``
*   `` 1 &lt;= target &lt;= 5000 ``