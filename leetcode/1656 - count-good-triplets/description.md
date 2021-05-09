Given an array of integers `` arr ``, and three integers&nbsp;`` a ``,&nbsp;`` b ``&nbsp;and&nbsp;`` c ``. You need to find the number of good triplets.

A triplet `` (arr[i], arr[j], arr[k]) ``&nbsp;is __good__ if the following conditions are true:

*   `` 0 &lt;= i &lt; j &lt; k &lt;&nbsp;arr.length ``
*   `` |arr[i] - arr[j]| &lt;= a ``
*   `` |arr[j] - arr[k]| &lt;= b ``
*   `` |arr[i] - arr[k]| &lt;= c ``

Where `` |x| `` denotes the absolute value of `` x ``.

Return_ the number of good triplets_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
<strong>Output:</strong> 4
<strong>Explanation:</strong>&nbsp;There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [1,1,2,2,3], a = 0, b = 0, c = 1
<strong>Output:</strong> 0
<strong>Explanation: </strong>No triplet satisfies all conditions.
</pre>

&nbsp;

__Constraints:__

*   `` 3 &lt;= arr.length &lt;= 100 ``
*   `` 0 &lt;= arr[i] &lt;= 1000 ``
*   `` 0 &lt;= a, b, c &lt;= 1000 ``