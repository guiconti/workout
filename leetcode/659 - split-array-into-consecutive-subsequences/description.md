Given an integer array `` nums `` that is __sorted in ascending order__, return `` true `` if and only if you can split it into __one or more__ subsequences such that each subsequence consists of consecutive integers and has a length of at least `` 3 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,3,3,4,5]
<strong>Output:</strong> true
<b>Explanation:</b>
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,2,3,3,4,4,5,5]
<strong>Output:</strong> true
<b>Explanation:</b>
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1,2,3,4,4,5]
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code>
*   `` -1000 &lt;= nums[i] &lt;= 1000 ``
*   `` nums `` is sorted in an __ascending__ order.