Given an array `` nums `` of __distinct__ positive integers, return _the number of tuples _`` (a, b, c, d) ``_ such that _`` a * b = c * d ``_ where _`` a ``_, _`` b ``_, _`` c ``_, and _`` d ``_ are elements of _`` nums ``_, and _`` a != b != c != d ``_._

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [2,3,4,6]
<strong>Output:</strong> 8
<strong>Explanation:</strong> There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,2,4,5,10]
<strong>Output:</strong> 16
<strong>Explanation:</strong> There are 16 valids tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,4,5)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [2,3,4,6,8,12]
<strong>Output:</strong> 40
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> nums = [2,3,5,7]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 1000 ``
*   <code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code>
*   All elements in `` nums `` are __distinct__.