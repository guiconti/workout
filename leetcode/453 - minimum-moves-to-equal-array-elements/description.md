Given an integer array `` nums `` of size `` n ``, return _the minimum number of moves required to make all array elements equal_.

In one move, you can increment `` n - 1 `` elements of the array by `` 1 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Only three moves are needed (remember each move increments two elements):
[1,2,3]  =&gt;  [2,3,3]  =&gt;  [3,4,3]  =&gt;  [4,4,4]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,1,1]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` n == nums.length ``
*   <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   <code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code>
*   The answer is guaranteed to fit in a __32-bit__ integer.