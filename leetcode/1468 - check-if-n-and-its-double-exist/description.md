Given an array `` arr `` of integers, check if there exists two integers `` N `` and `` M `` such that `` N `` is the double of `` M `` ( i.e. `` N = 2 * M ``).

More formally check if there exists&nbsp;two indices `` i `` and `` j `` such that :

*   `` i != j ``
*   `` 0 &lt;= i, j &lt; arr.length ``
*   `` arr[i] == 2 * arr[j] ``

&nbsp;

__Example 1:__

<strong>Input:</strong> arr = [10,2,5,3]
    <strong>Output:</strong> true
    <strong>Explanation:</strong> N = 10 is the double of M<code> = 5</code>,that is, <code>10 = 2 * 5</code>.

__Example 2:__

<strong>Input:</strong> arr = [7,1,14,11]
    <strong>Output:</strong> true
    <strong>Explanation:</strong> N = 14 is the double of M<code> = 7</code>,that is, <code>14 = 2 * 7</code>.

__Example 3:__

<pre>
<strong>Input:</strong> arr = [3,1,7,11]
<strong>Output:</strong> false
<strong>Explanation:</strong> In this case does not exist N and M, such that N = 2 * M.
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= arr.length &lt;= 500 ``
*   `` -10^3 &lt;= arr[i] &lt;= 10^3 ``