The __frequency__ of an element is the number of times it occurs in an array.

You are given an integer array `` nums `` and an integer `` k ``. In one operation, you can choose an index of `` nums `` and increment the element at that index by `` 1 ``.

Return _the __maximum possible frequency__ of an element after performing __at most__ _`` k ``_ operations_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,4], k = 5
<strong>Output:</strong> 3<strong>
Explanation:</strong> Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,4,8,13], k = 5
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [3,9,6], k = 2
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= k &lt;= 10<sup>5</sup></code>