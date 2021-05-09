You have a set of integers `` s ``, which originally contains all the numbers from `` 1 `` to `` n ``. Unfortunately, due to some error, one of the numbers in `` s `` got duplicated to another number in the set, which results in __repetition of one__ number and __loss of another__ number.

You are given an integer array `` nums `` representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return _them in the form of an array_.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> nums = [1,2,2,4]
<strong>Output:</strong> [2,3]
</pre>

__Example 2:__

<pre><strong>Input:</strong> nums = [1,1]
<strong>Output:</strong> [1,2]
</pre>

&nbsp;

__Constraints:__

*   <code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code>
*   <code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code>