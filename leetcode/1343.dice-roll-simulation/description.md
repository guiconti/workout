A die simulator generates a random number from 1 to 6 for each roll.&nbsp;You introduced a constraint to the generator such that it cannot roll the number `` i `` more than `` rollMax[i] `` (1-indexed) __consecutive__ times.&nbsp;

Given an array of integers&nbsp;`` rollMax ``&nbsp;and an integer&nbsp;`` n ``, return the number of distinct sequences that can be obtained with exact `` n `` rolls.

Two sequences are considered different if at least one element differs from each other. Since the answer&nbsp;may be too large,&nbsp;return it modulo `` 10^9 + 7 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 2, rollMax = [1,1,2,2,2,3]
<strong>Output:</strong> 34
<strong>Explanation:</strong> There will be 2 rolls of die, if there are no constraints on the die, there are 6 * 6 = 36 possible combinations. In this case, looking at rollMax array, the numbers 1 and 2 appear at most once consecutively, therefore sequences (1,1) and (2,2) cannot occur, so the final answer is 36-2 = 34.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 2, rollMax = [1,1,1,1,1,1]
<strong>Output:</strong> 30
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 3, rollMax = [1,1,1,2,2,3]
<strong>Output:</strong> 181
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 5000 ``
*   `` rollMax.length == 6 ``
*   `` 1 &lt;= rollMax[i] &lt;= 15 ``