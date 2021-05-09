You are given an integer array `` nums ``. The _value_ of this array is defined as the sum of `` |nums[i]-nums[i+1]| ``&nbsp;for all&nbsp;`` 0 &lt;= i &lt; nums.length-1 ``.

You are allowed to select any subarray of the given array and reverse it. You can perform this operation __only once__.

Find maximum possible value of the final array.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [2,3,1,5,4]
<strong>Output:</strong> 10
<b>Explanation: </b>By reversing the subarray [3,1,5] the array becomes [2,5,1,3,4] whose value is 10.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [2,4,9,24,2,1,10]
<strong>Output:</strong> 68
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 3*10^4 ``
*   `` -10^5 &lt;= nums[i] &lt;= 10^5 ``