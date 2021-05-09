You are given a sorted integer array `` arr `` containing `` 1 `` and __prime__ numbers, where all the integers of `` arr `` are unique. You are also given an integer `` k ``.

For every `` i `` and `` j `` where `` 0 &lt;= i &lt; j &lt; arr.length ``, we consider the fraction `` arr[i] / arr[j] ``.

Return _the_ <code>k<sup>th</sup></code> _smallest fraction considered_. Return your answer as an array of integers of size `` 2 ``, where `` answer[0] == arr[i] `` and `` answer[1] == arr[j] ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [1,2,3,5], k = 3
<strong>Output:</strong> [2,5]
<strong>Explanation:</strong> The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
The third fraction is 2/5.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [1,7], k = 1
<strong>Output:</strong> [1,7]
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= arr.length &lt;= 1000 ``
*   <code>1 &lt;= arr[i] &lt;= 3 * 10<sup>4</sup></code>
*   `` arr[0] == 1 ``
*   `` arr[i] `` is a __prime__ number for `` i &gt; 0 ``.
*   All the numbers of `` arr `` are __unique__ and sorted in __strictly increasing__ order.
*   `` 1 &lt;= k &lt;= arr.length * (arr.length - 1) / 2 ``