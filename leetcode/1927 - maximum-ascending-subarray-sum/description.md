Given an array of positive integers `` nums ``, return the _maximum possible sum of an __ascending__ subarray in _`` nums ``.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray <code>[nums<sub>l</sub>, nums<sub>l+1</sub>, ..., nums<sub>r-1</sub>, nums<sub>r</sub>]</code> is __ascending__ if for all `` i `` where `` l &lt;= i &lt; r ``, <code>nums<sub>i </sub> &lt; nums<sub>i+1</sub></code>. Note that a subarray of size `` 1 `` is __ascending__.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [10,20,30,5,10,50]
<strong>Output:</strong> 65
<strong>Explanation: </strong>[5,10,50] is the ascending subarray with the maximum sum of 65.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [10,20,30,40,50]
<strong>Output:</strong> 150
<strong>Explanation: </strong>[10,20,30,40,50] is the ascending subarray with the maximum sum of 150.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [12,17,15,13,10,11,12]
<strong>Output:</strong> 33
<strong>Explanation: </strong>[10,11,12] is the ascending subarray with the maximum sum of 33.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> nums = [100,10,1]
<strong>Output:</strong> 100
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 100 ``
*   `` 1 &lt;= nums[i] &lt;= 100 ``