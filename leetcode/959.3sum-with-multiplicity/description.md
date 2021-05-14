Given an integer array `` arr ``, and an integer `` target ``, return the number of tuples `` i, j, k `` such that `` i &lt; j &lt; k `` and `` arr[i] + arr[j] + arr[k] == target ``.

As the answer can be very large, return it __modulo__ <code>10<sup>9</sup> + 7</code>.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [1,1,2,2,3,3,4,4,5,5], target = 8
<strong>Output:</strong> 20
<strong>Explanation: </strong>
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [1,1,2,2,2,2], target = 5
<strong>Output:</strong> 12
<strong>Explanation: </strong>
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.
</pre>

&nbsp;

__Constraints:__

*   `` 3 &lt;= arr.length &lt;= 3000 ``
*   `` 0 &lt;= arr[i] &lt;= 100 ``
*   `` 0 &lt;= target &lt;= 300 ``