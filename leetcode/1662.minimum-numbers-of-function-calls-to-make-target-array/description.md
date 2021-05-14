<img alt="" src="https://assets.leetcode.com/uploads/2020/07/10/sample_2_1887.png" style="width: 573px; height: 294px;"/>

Your task is to form&nbsp;an integer array `` nums `` from an initial array of zeros&nbsp;`` arr `` that is the&nbsp;same size&nbsp;as `` nums ``.

Return the minimum number of&nbsp;function calls to make `` nums `` from `` arr ``.

The answer is guaranteed to fit in a 32-bit signed integer.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,5]
<strong>Output:</strong> 5
<strong>Explanation:</strong> Increment by 1 (second element): [0, 0] to get [0, 1] (1 operation).
Double all the elements: [0, 1] -&gt; [0, 2] -&gt; [0, 4] (2 operations).
Increment by 1 (both elements)  [0, 4] -&gt; [1, 4] -&gt; <strong>[1, 5]</strong> (2 operations).
Total of operations: 1 + 2 + 2 = 5.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [2,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Increment by 1 (both elements) [0, 0] -&gt; [0, 1] -&gt; [1, 1] (2 operations).
Double all the elements: [1, 1] -&gt; <strong>[2, 2]</strong> (1 operation).
Total of operations: 2 + 1 = 3.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [4,2,5]
<strong>Output:</strong> 6
<strong>Explanation:</strong> (initial)[0,0,0] -&gt; [1,0,0] -&gt; [1,0,1] -&gt; [2,0,2] -&gt; [2,1,2] -&gt; [4,2,4] -&gt; <strong>[4,2,5]</strong>(nums).
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> nums = [3,2,2,4]
<strong>Output:</strong> 7
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> nums = [2,4,8,16]
<strong>Output:</strong> 8
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 10^5 ``
*   `` 0 &lt;= nums[i] &lt;= 10^9 ``