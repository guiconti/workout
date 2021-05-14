Given an array of integers `` arr `` of even length `` n `` and an integer `` k ``.

We want to divide the array into exactly `` n /&nbsp;2 `` pairs such that the sum of each pair is divisible by `` k ``.

Return _True_ If you can find a way to do that or _False_ otherwise.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [1,2,3,4,5,10,6,7,8,9], k = 5
<strong>Output:</strong> true
<strong>Explanation:</strong> Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [1,2,3,4,5,6], k = 7
<strong>Output:</strong> true
<strong>Explanation:</strong> Pairs are (1,6),(2,5) and(3,4).
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [1,2,3,4,5,6], k = 10
<strong>Output:</strong> false
<strong>Explanation:</strong> You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> arr = [-10,10], k = 2
<strong>Output:</strong> true
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> arr = [-1,1,-2,2,-3,3,-4,4], k = 3
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   `` arr.length == n ``
*   <code>1 &lt;= n &lt;= 10<sup>5</sup></code>
*   `` n `` is even.
*   <code>-10<sup>9</sup> &lt;= arr[i] &lt;= 10<sup>9</sup></code>
*   <code>1 &lt;= k &lt;= 10<sup>5</sup></code>