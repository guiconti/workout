For an integer array `` nums ``, an __inverse pair__ is a pair of integers `` [i, j] `` where `` 0 &lt;= i &lt; j &lt; nums.length `` and `` nums[i] &gt; nums[j] ``.

Given two integers n and k, return the number of different arrays consist of numbers from `` 1 `` to `` n `` such that there are exactly `` k `` __inverse pairs__. Since the answer can be huge, return it __modulo__ <code>10<sup>9</sup> + 7</code>.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 3, k = 0
<strong>Output:</strong> 1
<strong>Explanation:</strong> Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 3, k = 1
<strong>Output:</strong> 2
<strong>Explanation:</strong> The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 1000 ``
*   `` 0 &lt;= k &lt;= 1000 ``