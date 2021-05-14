You are given an array `` people `` where `` people[i] `` is the weight of the <code>i<sup>th</sup></code> person, and an __infinite number of boats__ where each boat can carry a maximum weight of `` limit ``. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most `` limit ``.

Return _the minimum number of boats to carry every given person_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> people = [1,2], limit = 3
<strong>Output:</strong> 1
<strong>Explanation:</strong> 1 boat (1, 2)
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> people = [3,2,2,1], limit = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> 3 boats (1, 2), (2) and (3)
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> people = [3,5,3,4], limit = 5
<strong>Output:</strong> 4
<strong>Explanation:</strong> 4 boats (3), (3), (4), (5)
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= people.length &lt;= 5 * 10<sup>4</sup></code>
*   <code>1 &lt;= people[i] &lt;= limit &lt;= 3 * 10<sup>4</sup></code>