You are given a __sorted unique__ integer array `` nums ``.

Return _the __smallest sorted__ list of ranges that __cover all the numbers in the array exactly___. That is, each element of `` nums `` is covered by exactly one of the ranges, and there is no integer `` x `` such that `` x `` is in one of the ranges but not in `` nums ``.

Each range `` [a,b] `` in the list should be output as:

*   `` "a-&gt;b" `` if `` a != b ``
*   `` "a" `` if `` a == b ``

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [0,1,2,4,5,7]
<strong>Output:</strong> ["0-&gt;2","4-&gt;5","7"]
<strong>Explanation:</strong> The ranges are:
[0,2] --&gt; "0-&gt;2"
[4,5] --&gt; "4-&gt;5"
[7,7] --&gt; "7"
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [0,2,3,4,6,8,9]
<strong>Output:</strong> ["0","2-&gt;4","6","8-&gt;9"]
<strong>Explanation:</strong> The ranges are:
[0,0] --&gt; "0"
[2,4] --&gt; "2-&gt;4"
[6,6] --&gt; "6"
[8,9] --&gt; "8-&gt;9"
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = []
<strong>Output:</strong> []
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> nums = [-1]
<strong>Output:</strong> ["-1"]
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> nums = [0]
<strong>Output:</strong> ["0"]
</pre>

&nbsp;

__Constraints:__

*   `` 0 &lt;= nums.length &lt;= 20 ``
*   <code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code>
*   All the values of `` nums `` are __unique__.
*   `` nums `` is sorted in ascending order.