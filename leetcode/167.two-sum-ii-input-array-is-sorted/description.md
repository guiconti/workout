Given an array of integers `` numbers `` that is already ___sorted in ascending order___, find two numbers such that they add up to a specific `` target `` number.

Return the indices of the two numbers (__1-indexed__) as an integer array `` answer `` of size `` 2 ``, where `` 1 &lt;= answer[0] &lt; answer[1] &lt;= numbers.length ``.

You may assume that each input would have __exactly one solution__ and you __may not__ use the same element twice.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> numbers = [2,7,11,15], target = 9
<strong>Output:</strong> [1,2]
<strong>Explanation:</strong> The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> numbers = [2,3,4], target = 6
<strong>Output:</strong> [1,3]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> numbers = [-1,0], target = -1
<strong>Output:</strong> [1,2]
</pre>

&nbsp;

__Constraints:__

*   <code>2 &lt;= numbers.length &lt;= 3 * 10<sup>4</sup></code>
*   `` -1000 &lt;= numbers[i] &lt;= 1000 ``
*   `` numbers `` is sorted in __increasing order__.
*   `` -1000 &lt;= target &lt;= 1000 ``
*   __Only one valid answer exists.__