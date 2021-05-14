Given an integer array&nbsp;`` nums ``, return _the number of longest increasing subsequences._

__Notice__ that the sequence has to be __strictly__ increasing.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,3,5,4,7]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [2,2,2,2,2]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 2000 ``
*   <code>-10<sup>6</sup> &lt;= nums[i] &lt;= 10<sup>6</sup></code>