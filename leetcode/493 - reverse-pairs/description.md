Given an integer array `` nums ``, return _the number of __reverse pairs__ in the array_.

A reverse pair is a pair `` (i, j) `` where `` 0 &lt;= i &lt; j &lt; nums.length `` and `` nums[i] &gt; 2 * nums[j] ``.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> nums = [1,3,2,3,1]
<strong>Output:</strong> 2
</pre>

__Example 2:__

<pre><strong>Input:</strong> nums = [2,4,3,5,1]
<strong>Output:</strong> 3
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code>
*   <code>2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code>