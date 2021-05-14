You are given an integer array `` nums `` of length `` n ``.

Assume <code>arr<sub>k</sub></code> to be an array obtained by rotating `` nums `` by `` k `` positions clock-wise. We define the __rotation function__ `` F `` on `` nums `` as follow:

*   <code>F(k) = 0 * arr<sub>k</sub>[0] + 1 * arr<sub>k</sub>[1] + ... + (n - 1) * arr<sub>k</sub>[n - 1].</code>

Return _the maximum value of_ `` F(0), F(1), ..., F(n-1) ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [4,3,2,6]
<strong>Output:</strong> 26
<strong>Explanation:</strong>
F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1000000007]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` n == nums.length ``
*   <code>1 &lt;= n &lt;= 10<sup>5</sup></code>
*   <code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code>