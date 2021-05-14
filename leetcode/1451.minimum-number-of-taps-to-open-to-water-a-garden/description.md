There is a one-dimensional garden on the x-axis. The garden starts at the point `` 0 `` and ends at the point `` n ``. (i.e The length of the garden is `` n ``).

There are&nbsp;`` n + 1 `` taps located&nbsp;at points `` [0, 1, ..., n] `` in the garden.

Given an integer `` n `` and an integer array `` ranges `` of length `` n + 1 `` where `` ranges[i] `` (0-indexed) means the `` i-th `` tap can water the area `` [i - ranges[i], i + ranges[i]] `` if it was open.

Return _the minimum number of taps_ that should be open to water the whole garden, If the garden cannot be watered return __-1__.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/01/16/1685_example_1.png" style="width: 525px; height: 255px;"/>

<pre>
<strong>Input:</strong> n = 5, ranges = [3,4,1,1,0,0]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The tap at point 0 can cover the interval [-3,3]
The tap at point 1 can cover the interval [-3,5]
The tap at point 2 can cover the interval [1,3]
The tap at point 3 can cover the interval [2,4]
The tap at point 4 can cover the interval [4,4]
The tap at point 5 can cover the interval [5,5]
Opening Only the second tap will water the whole garden [0,5]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 3, ranges = [0,0,0,0]
<strong>Output:</strong> -1
<strong>Explanation:</strong> Even if you activate all the four taps you cannot water the whole garden.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 7, ranges = [1,2,1,0,2,1,0,1]
<strong>Output:</strong> 3
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> n = 8, ranges = [4,0,0,0,0,0,0,0,4]
<strong>Output:</strong> 2
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> n = 8, ranges = [4,0,0,0,4,0,0,0,4]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 10^4 ``
*   `` ranges.length == n + 1 ``
*   `` 0 &lt;= ranges[i] &lt;= 100 ``