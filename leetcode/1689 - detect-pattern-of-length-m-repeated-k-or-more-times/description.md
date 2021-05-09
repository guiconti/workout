Given an array of positive integers `` arr ``,&nbsp; find a pattern of length `` m `` that is repeated `` k `` or more times.

A __pattern__ is a subarray (consecutive sub-sequence) that consists of one or more values, repeated multiple times __consecutively __without overlapping. A pattern is defined by its length and the number of repetitions.

Return&nbsp;`` true ``&nbsp;_if there exists a pattern of length_&nbsp;`` m ``&nbsp;_that is repeated_&nbsp;`` k ``&nbsp;_or more times, otherwise return_&nbsp;`` false ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [1,2,4,4,4,4], m = 1, k = 3
<strong>Output:</strong> true
<strong>Explanation: </strong>The pattern <strong>(4)</strong> of length 1 is repeated 4 consecutive times. Notice that pattern can be repeated k or more times but not less.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [1,2,1,2,1,1,1,3], m = 2, k = 2
<strong>Output:</strong> true
<strong>Explanation: </strong>The pattern <strong>(1,2)</strong> of length 2 is repeated 2 consecutive times. Another valid pattern <strong>(2,1) is</strong> also repeated 2 times.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [1,2,1,2,1,3], m = 2, k = 3
<strong>Output:</strong> false
<strong>Explanation: </strong>The pattern (1,2) is of length 2 but is repeated only 2 times. There is no pattern of length 2 that is repeated 3 or more times.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> arr = [1,2,3,1,2], m = 2, k = 2
<strong>Output:</strong> false
<strong>Explanation: </strong>Notice that the pattern (1,2) exists twice but not consecutively, so it doesn't count.
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> arr = [2,2,2,2], m = 2, k = 3
<strong>Output:</strong> false
<strong>Explanation: </strong>The only pattern of length 2 is (2,2) however it's repeated only twice. Notice that we do not count overlapping repetitions.
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= arr.length &lt;= 100 ``
*   `` 1 &lt;= arr[i] &lt;= 100 ``
*   `` 1 &lt;= m&nbsp;&lt;= 100 ``
*   `` 2 &lt;= k&nbsp;&lt;= 100 ``