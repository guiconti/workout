Given an integer array `` nums `` of size `` n ``, return _the minimum number of moves required to make all array elements equal_.

In one move, you can increment or decrement an element of the array by `` 1 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
Only two moves are needed (remember each move increments or decrements one element):
[<u>1</u>,2,3]  =&gt;  [2,2,<u>3</u>]  =&gt;  [2,2,2]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,10,2,9]
<strong>Output:</strong> 16
</pre>

&nbsp;

__Constraints:__

*   `` n == nums.length ``
*   <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   <code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code>