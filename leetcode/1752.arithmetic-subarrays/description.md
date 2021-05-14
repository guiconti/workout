A sequence of numbers is called __arithmetic__ if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a sequence `` s `` is arithmetic if and only if `` s[i+1] - s[i] == s[1] - s[0]  ``for all valid `` i ``.

For example, these are __arithmetic__ sequences:

<pre>
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9</pre>

The following sequence is not __arithmetic__:

<pre>
1, 1, 2, 5, 7</pre>

You are given an array of `` n `` integers, `` nums ``, and two arrays of `` m `` integers each, `` l `` and `` r ``, representing the `` m `` range queries, where the <code>i<sup>th</sup></code> query is the range `` [l[i], r[i]] ``. All the arrays are __0-indexed__.

Return _a list of _`` boolean `` _elements_ `` answer ``_, where_ `` answer[i] `` _is_ `` true `` _if the subarray_ `` nums[l[i]], nums[l[i]+1], ... , nums[r[i]] ``_ can be __rearranged__ to form an __arithmetic__ sequence, and_ `` false `` _otherwise._

&nbsp;

__Example 1:__

<strong>Input:</strong> nums = [4,6,5,9,3,7], l = <code>[0,0,2]</code>, r = <code>[2,3,5]</code>
<strong>Output:</strong> <code>[true,false,true]</code>
<strong>Explanation:</strong>
    In the 0<sup>th</sup> query, the subarray is [4,6,5]. This can be rearranged as [6,5,4], which is an arithmetic sequence.
    In the 1<sup>st</sup> query, the subarray is [4,6,5,9]. This cannot be rearranged as an arithmetic sequence.
    In the 2<sup>nd</sup> query, the subarray is <code>[5,9,3,7]. This</code> can be rearranged as <code>[3,5,7,9]</code>, which is an arithmetic sequence.

__Example 2:__

<pre>
<strong>Input:</strong> nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]
<strong>Output:</strong> [false,true,false,false,true,true]
</pre>

&nbsp;

__Constraints:__

*   `` n == nums.length ``
*   `` m == l.length ``
*   `` m == r.length ``
*   `` 2 &lt;= n &lt;= 500 ``
*   `` 1 &lt;= m &lt;= 500 ``
*   `` 0 &lt;= l[i] &lt; r[i] &lt; n ``
*   <code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code>